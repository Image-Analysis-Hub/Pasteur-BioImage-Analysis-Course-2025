import numpy as np
import napari
from napari.qt import QtViewerButtons

from skimage import io
from skimage.exposure import rescale_intensity
from superqt import QLabeledSlider
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel
from pathlib import Path
from typing import List, Union
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from detect_spots import DetectionPipeline
import re


dt = DetectionPipeline()


class SpotsThresholding:
    """
    Tool used to find in a semi automated way the spots.
    
    
    06/05/25    Jacques BOURG    
    """
    def __init__(
        self,
        BATCH: List[
            Union[Path, str]
        ],  # images are supposed to have only one channel (they can be 2D or 3D)
        BATCH_NAME="",
        voxel_size_nm=(
            300,
            103,
            103,
        ),  # use this for 3D and omit the first value for 2D
        object_radius_nm=(350, 150, 150),
        spots_other_method=None,
        subtract_fish=True,
    ):
        self.current_image_index = 0
        self.voxel_size_nm = voxel_size_nm
        self.object_radius_nm = object_radius_nm
        self.BATCH = BATCH
        self.BATCH_NAME = BATCH_NAME
        self.subtract_fish = subtract_fish
        name = np.array(self.BATCH).flatten()[self.current_image_index].stem
        if self.subtract_fish:
            name = re.sub(r"_FISH_\d+", "", name)
        self.name_im = name

        im = io.imread(np.array(self.BATCH).flatten()[self.current_image_index])

        self.im_fish = im  # [..., self.channel_fish]  # 2 or 3D

        if self.im_fish.ndim == 3:  # test whether the image is 2D or 3D
            mip = np.max(self.im_fish, axis=0)
            val = np.percentile(mip, 99) 
            self.im_fish_mpi = rescale_intensity(mip, in_range=(0, val))
        else:
            val = np.percentile(self.im_fish, 99) 
            self.im_fish_mpi = rescale_intensity(self.im_fish.copy(), in_range=(0, val))      

        self.list_im = np.array(self.BATCH).flatten()
        names = [el.stem for el in np.array(self.BATCH).flatten()]
        if self.subtract_fish:
            names = [re.sub(r"_FISH_\d+", "", name) for name in names]

        self.detected_spots = {name: [] for name in names}
        self.detected_spots_2d = {name: [] for name in names}
        
        thresholds, count_spots, threshold = dt.spot_big_fish_thresh_count_threshold(
            self.im_fish,
            voxel_size_nm=self.voxel_size_nm,
            object_radius_nm=self.object_radius_nm,
        )
        self.min_thresh = thresholds[0]
        self.max_thresh = thresholds[-1]

        thresholds_list = [[] for el in np.array(self.BATCH).flatten()]
        count_spots_list = [[] for el in np.array(self.BATCH).flatten()]

        self.thresholds_list = thresholds_list
        self.count_spots_list = count_spots_list
        self.thresholds_list[self.current_image_index] = thresholds
        self.count_spots_list[self.current_image_index] = count_spots

        self.thresh_spot = np.full(len(self.list_im), np.nan)
        self.thresh_spot[self.current_image_index] = int(threshold)

        #self.ind_init_threshold = self.find_index(thresholds, threshold)
        self.ind_actual_threshold = self.find_index(thresholds, threshold)

        dict_thresh_spot = {name: np.nan for name in names}
        self.dict_thresh_spot = dict_thresh_spot
        self.dict_thresh_spot[self.name_im] = threshold

        self.detected_spots[self.name_im] = dt.spot_bigfish(
            self.im_fish,
            voxel_size_nm=self.voxel_size_nm,
            object_radius_nm=self.object_radius_nm,
            thresh=self.thresh_spot[self.current_image_index],
        )
        if self.im_fish.ndim == 3:  # test whether the image is 2D or 3D
            self.detected_spots_2d = {key: value[:, 1:3] if hasattr(value, 'shape') and len(value.shape) == 2 and value.shape[1] >= 3 else value
                                            for key, value in self.detected_spots.items()}
        else:
            self.detected_spots_2d = self.detected_spots.copy()

        self.spots_other_method = {}
        if spots_other_method is not None:
            if self.im_fish.ndim == 3:
                self.spots_other_method = {key: value[:, 1:3] if hasattr(value, 'shape') and len(value.shape) == 2 and value.shape[1] >= 3 else value
                                            for key, value in spots_other_method.items()}
            elif self.im_fish.ndim == 2:
                self.spots_other_method = spots_other_method
            
        self.fig, self.ax = plt.subplots()
        self.ax.plot(thresholds, count_spots)
        # self.ax.plot(
        #     [thresholds[self.ind_init_threshold], thresholds[self.ind_init_threshold]],
        #     [
        #         count_spots[self.ind_init_threshold],
        #         count_spots[self.ind_init_threshold],
        #     ],
        #     "ro",
        # )
        self.ax.plot(
            [
                thresholds[self.ind_actual_threshold],
                thresholds[self.ind_actual_threshold],
            ],
            [
                count_spots[self.ind_actual_threshold],
                count_spots[self.ind_actual_threshold],
            ],
            "bo",
        )
        self.ax.set_ylabel("\n   Count Spots (log scale)", fontsize=10)
        self.ax.set_xlabel("Thresholds", fontsize=10)
        self.ax.set_title("Log(Count Spots) vs Thresholds", fontsize=10)
        #self.fig.tight_layout()  # Add tight layout to prevent clipping of labels
        # Create a FigureCanvas object
        self.canvas = FigureCanvas(self.fig)

    def find_index(self, thresholds, threshold):
        return  np.argmin((np.array(thresholds) - threshold)**2)  # np.where(thresholds == threshold)[0][0]

    def change_image(self, viewer, button, my_slider):
        """
        Function to change the displayed image and update the threshold accordingly.

        Args:
            viewer: The napari viewer instance.
            current_image_index: The index of the currently displayed image.
            button: The button that triggered the change.
        """

        self.current_image_index = int(
            (self.current_image_index + 1) % len(self.list_im)
        )
        button.setText(f"Image {self.current_image_index}")

        if (self.list_im[self.current_image_index] is not None) and (self.list_im[self.current_image_index] != Path('.')):
            im = io.imread(self.list_im[self.current_image_index])
            self.im_fish = im  # [..., self.channel_fish]

            if self.im_fish.ndim == 3:  # test whether the image is 2D or 3D
                mip = np.max(self.im_fish, axis=0)
                val = np.percentile(mip, 99) 
                self.im_fish_mpi = rescale_intensity(mip, in_range=(0, val))
            else:
                self.im_fish_mpi = self.im_fish

            name = np.array(self.BATCH).flatten()[self.current_image_index].stem
            if self.subtract_fish:
                name = re.sub(r"_FISH_\d+", "", name)
            self.name_im = name

            viewer.layers[0].data = self.im_fish_mpi
            viewer.layers[0].name = f"FISH {self.name_im}"    

            if not np.isnan(self.thresh_spot[self.current_image_index]):
                self.detected_spots[self.name_im] = dt.spot_bigfish(
                    self.im_fish,
                    voxel_size_nm=self.voxel_size_nm,
                    object_radius_nm=self.object_radius_nm,
                    thresh=self.thresh_spot[self.current_image_index],
                )
                if self.im_fish.ndim == 3:  # test whether the image is 2D or 3D
                    self.detected_spots_2d = {key: value[:, 1:3] if hasattr(value, 'shape') and len(value.shape) == 2 and value.shape[1] >= 3 else value
                                            for key, value in self.detected_spots.items()}
                else:
                    self.detected_spots_2d = self.detected_spots.copy()
                    
                viewer.layers[1].data = self.detected_spots_2d[self.name_im]
                if len(self.spots_other_method) != 0:
                    viewer.layers[2].data  = self.spots_other_method[self.name_im]

                self.min_thresh = self.thresholds_list[self.current_image_index][0]
                self.max_thresh = self.thresholds_list[self.current_image_index][-1]
                my_slider.setMinimum(int(self.min_thresh))
                my_slider.setMaximum(int(self.max_thresh))
                my_slider.setValue(int(self.thresh_spot[self.current_image_index]))

            else:
                thresholds, count_spots, threshold = (
                    dt.spot_big_fish_thresh_count_threshold(
                        self.im_fish,
                        voxel_size_nm=self.voxel_size_nm,
                        object_radius_nm=self.object_radius_nm,
                    )
                )
                self.thresholds_list[self.current_image_index] = thresholds
                self.count_spots_list[self.current_image_index] = count_spots
                self.thresh_spot[self.current_image_index] = int(threshold)
                self.dict_thresh_spot[self.name_im] = int(threshold)
                self.min_thresh = thresholds[0]
                self.max_thresh = thresholds[-1]
                my_slider.setMinimum(int(self.min_thresh))
                my_slider.setMaximum(int(self.max_thresh))

                my_slider.setValue(int(self.thresh_spot[self.current_image_index]))
                self.detected_spots[self.name_im] = dt.spot_bigfish(
                    self.im_fish,
                    voxel_size_nm=self.voxel_size_nm,
                    object_radius_nm=self.object_radius_nm,
                    thresh=self.thresh_spot[self.current_image_index],
                )
                self.detected_spots_2d = {key: value[:, 1:3] if hasattr(value, 'shape') and len(value.shape) == 2 and value.shape[1] >= 3 else value
                                            for key, value in self.detected_spots.items()}
                viewer.layers[1].data = self.detected_spots_2d[self.name_im]
                if self.im_fish.ndim == 3:  # test whether the image is 2D or 3D
                    self.detected_spots_2d = {key: value[:, 1:3] if hasattr(value, 'shape') and len(value.shape) == 2 and value.shape[1] >= 3 else value
                                            for key, value in self.detected_spots.items()}
                else:
                    self.detected_spots_2d = self.detected_spots.copy()                
                
                if len(self.spots_other_method) != 0:
                    viewer.layers[2].data  = self.spots_other_method[self.name_im]

            thresholds = self.thresholds_list[self.current_image_index]
            count_spots = self.count_spots_list[self.current_image_index]
            threshold = self.thresh_spot[self.current_image_index]

            #self.ind_init_threshold = self.find_index(thresholds, threshold)
            self.ind_actual_threshold = self.find_index(thresholds, threshold)

            self.ax.clear()
            self.ax.plot(thresholds, count_spots)
            # self.ax.plot(
            #     [thresholds[self.ind_init_threshold], thresholds[self.ind_init_threshold]],
            #     [
            #         count_spots[self.ind_init_threshold],
            #         count_spots[self.ind_init_threshold],
            #     ],
            #     "ro",
            # )
            self.ax.plot(
                [
                    thresholds[self.ind_actual_threshold],
                    thresholds[self.ind_actual_threshold],
                ],
                [
                    count_spots[self.ind_actual_threshold],
                    count_spots[self.ind_actual_threshold],
                ],
                "bo",
            )
            self.ax.set_ylabel("Count Spots (log scale)", fontsize=10)
            self.ax.set_xlabel("Thresholds", fontsize=10)
            self.ax.set_title("Log (Count Spots) vs Thresholds", fontsize=10)
            self.canvas.draw()

        else:
            viewer.layers[0].data  = np.zeros((100,100))
            viewer.layers[1].data  = []
            if len(self.spots_other_method) != 0:
                viewer.layers[2].data  = []

            self.ax.clear()
            self.canvas.draw()
            
            
    def update_threshold(self, viewer, image, threshold):
        """
        On a slider change, update the threshold value.

        Args:
            viewer: The napari viewer instance.
            threshold1: The intensity threshold value.
        """
        if (self.list_im[self.current_image_index] is not None) and (self.list_im[self.current_image_index] != Path('.')):
            self.thresh_spot[self.current_image_index] = int(threshold)
            self.detected_spots[self.name_im] = dt.spot_bigfish(
                self.im_fish,
                voxel_size_nm=self.voxel_size_nm,
                object_radius_nm=self.object_radius_nm,
                thresh=threshold,
            )
            if self.im_fish.ndim == 3:  # test whether the image is 2D or 3D
                self.detected_spots_2d = {key: value[:, 1:3] if hasattr(value, 'shape') and len(value.shape) == 2 and value.shape[1] >= 3 else value                                            for key, value in self.detected_spots.items()}
            else:
                self.detected_spots_2d = self.detected_spots.copy()    
            viewer.layers[1].data = self.detected_spots_2d[self.name_im]     
            self.thresh_spot[self.current_image_index] = int(threshold)
            self.dict_thresh_spot[self.name_im] = int(threshold)

            self.ind_actual_threshold = self.find_index(
                self.thresholds_list[self.current_image_index], threshold
            )

            self.ax.clear()
            self.ax.plot(
                self.thresholds_list[self.current_image_index],
                self.count_spots_list[self.current_image_index],
            )
            # self.ax.plot(
            #     [
            #         self.thresholds_list[self.current_image_index][self.ind_init_threshold],
            #         self.thresholds_list[self.current_image_index][self.ind_init_threshold],
            #     ],
            #     [
            #         self.count_spots_list[self.current_image_index][
            #             self.ind_init_threshold
            #         ],
            #         self.count_spots_list[self.current_image_index][
            #             self.ind_init_threshold
            #         ],
            #     ],
            #     "ro",
            # )
            self.ax.plot(
                [
                    self.thresholds_list[self.current_image_index][
                        self.ind_actual_threshold
                    ],
                    self.thresholds_list[self.current_image_index][
                        self.ind_actual_threshold
                    ],
                ],
                [
                    self.count_spots_list[self.current_image_index][
                        self.ind_actual_threshold
                    ],
                    self.count_spots_list[self.current_image_index][
                        self.ind_actual_threshold
                    ],
                ],
                "bo",
            )
            self.ax.set_ylabel("Count Spots", fontsize=10)
            self.ax.set_xlabel("Thresholds", fontsize=10)
            self.ax.set_title("Log(Count Spots) vs Thresholds", fontsize=10)
            self.canvas.draw()

        
        
    def run(self):
        """
        Sets up the Napari viewer and starts the interactive thresholding process.
        """
        viewer = napari.Viewer(title=self.BATCH_NAME)

        # set the layers
        viewer.add_image(self.im_fish_mpi, rgb=False, name=f"FISH {self.name_im}")
        viewer.add_points(
            self.detected_spots_2d[self.name_im],
            name="spots",
            size=4,
            border_color='#0000FF',
            face_color=[0, 0, 0, 0],
        )

        if len(self.spots_other_method) != 0:
            viewer.add_points(
            self.spots_other_method[self.name_im],
            name="spots UFISH",
            size=2,
            face_color='green',
            opacity=0.5,
        )

        button_widget = QtViewerButtons(
            viewer
        )  # This creates the standard napari buttons
        my_button = QPushButton("Image 0: next image")
        my_button.setFixedSize(300, 30)

        # Create the slider Intensity
        my_slider = QLabeledSlider(Qt.Orientation.Horizontal)
        my_slider.setMinimum(int(self.min_thresh))
        my_slider.setMaximum(int(self.max_thresh))
        my_slider.setFixedWidth(500)
        my_slider.sliderReleased.connect(
            lambda: self.update_threshold(viewer, self.im_fish, my_slider.value())
        )

        my_slider.setValue(int(self.thresh_spot[self.current_image_index]))

        # button : change image
        my_button.clicked.connect(
            lambda: self.change_image(viewer, my_button, my_slider)
        )
        button_widget.layout().addWidget(my_button)  # Add it to the existing layout

        # Create a custom widget with a larger label
        widget = QWidget()
        layout = QVBoxLayout()
        title_label = QLabel("Spot threshold")
        title_label.setStyleSheet("font-size: 12pt")  # Adjust size as needed
        layout.addWidget(title_label)
        layout.addWidget(my_slider)
        layout.setContentsMargins(10, 0, 50, 0)
        widget.setLayout(layout)
        viewer.window.add_dock_widget(widget, area="bottom")
        viewer.window.add_dock_widget(
            button_widget,
            area="bottom",
            name="Viewer Buttons",
        )  # Standard buttons + custom

        button_widget.setFixedWidth(500) # 1500

        # Add the Matplotlib plot as a dock widget
        plot_widget = QWidget()
        plot_widget.setFixedWidth(200) # 400
        plot_widget.setFixedHeight(200)
        plot_layout = QVBoxLayout()
        plot_layout.addWidget(self.canvas)
        plot_widget.setLayout(plot_layout)
        viewer.window.add_dock_widget(plot_widget, area="bottom", name="Histogram")

        napari.run()
