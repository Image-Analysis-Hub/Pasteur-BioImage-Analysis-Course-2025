import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from scipy.ndimage import correlate
import matplotlib.colors as mcolors

class ConvolutionExplorer:
    """Tool to explore and understand the convolution.
        Jacques Bourg 02.05.2025  Neubias course
    """
    
    def __init__(self, initial_image):
        
        # define the kernels
        kernel1 = np.zeros((11, 11))
        kernel1[5 - 5:5 + 5 + 1, 5] = 1
        kernel1[5, 5 - 5:5 + 5 + 1] = 1

        kernel2 = np.zeros((11, 11))
        kernel2[5, 5] = 1

        kernel3 = np.zeros((11, 11))
        kernel3[4:7, 4:7] = 1

        kernel4 = np.zeros((11, 11))
        kernel4[:, 5] = 1

        kernel5 = np.zeros((13, 13))
        kernel5[5:8, 5:8] = -1 / 8
        kernel5[6, 6] = 1

        kernel6 = np.zeros((11, 11))
        kernel6[3:8, 3:8] = -9 / 12
        kernel6[4:7, 4:7] = 1

        kernel7 = np.zeros((13, 13))
        lp = 6
        kernel7[6 - lp:6 + lp + 1, 5] = -21 / 48
        kernel7[6 - lp:6 + lp + 1, 6] = -21 / 48
        kernel7[6 - lp:6 + lp + 1, 7] = -21 / 48
        kernel7[5, 6 - lp:6 + lp + 1] = -21 / 48
        kernel7[6, 6 - lp:6 + lp + 1] = -21 / 48
        kernel7[7, 6 - lp:6 + lp + 1] = -21 / 48
        kernel7[6 - 5:6 + 5 + 1, 6] = 1
        kernel7[6, 6 - 5:6 + 5 + 1] = 1

        kernel8 = np.zeros((11, 11))
        kernel8[:, 3:8] = 1
        kernel8[:, 4:7] = -22 / 33

        kernel9 = np.zeros((15, 15))
        lpp = 7
        kernel9[7 - lpp:7 + lpp + 1, 5] = -69 / 56
        kernel9[7 - lpp:7 + lpp + 1, 6] = -69 / 56
        kernel9[7 - lpp:7 + lpp + 1, 7] = -69 / 56
        kernel9[7 - lpp:7 + lpp + 1, 8] = -69 / 56
        kernel9[7 - lpp:7 + lpp + 1, 9] = -69 / 56
        kernel9[5, 7 - lpp:7 + lpp + 1] = -69 / 56
        kernel9[6, 7 - lpp:7 + lpp + 1] = -69 / 56
        kernel9[7, 7 - lpp:7 + lpp + 1] = -69 / 56
        kernel9[8, 7 - lpp:7 + lpp + 1] = -69 / 56
        kernel9[9, 7 - lpp:7 + lpp + 1] = -69 / 56

        lp = 6
        kernel9[7 - lp:7 + lp + 1, 6] = 1
        kernel9[7 - lp:7 + lp + 1, 7] = 1
        kernel9[7 - lp:7 + lp + 1, 8] = 1
        kernel9[6, 7 - lp:7 + lp + 1] = 1
        kernel9[7, 7 - lp:7 + lp + 1] = 1
        kernel9[8, 7 - lp:7 + lp + 1] = 1

        kernel10 = np.zeros((15, 15))
        lpp = 7
        kernel10[7 - lpp:7 + lpp + 1, 5] = -21 / 104
        kernel10[7 - lpp:7 + lpp + 1, 6] = -21 / 104
        kernel10[7 - lpp:7 + lpp + 1, 7] = -21 / 104
        kernel10[7 - lpp:7 + lpp + 1, 8] = -21 / 104
        kernel10[7 - lpp:7 + lpp + 1, 9] = -21 / 104
        kernel10[5, 7 - lpp:7 + lpp + 1] = -21 / 104
        kernel10[6, 7 - lpp:7 + lpp + 1] = -21 / 104
        kernel10[7, 7 - lpp:7 + lpp + 1] = -21 / 104
        kernel10[8, 7 - lpp:7 + lpp + 1] = -21 / 104
        kernel10[9, 7 - lpp:7 + lpp + 1] = -21 / 104
        lp = 5
        kernel10[7 - lp:7 + lp + 1, 7] = 1
        kernel10[7, 7 - lp:7 + lp + 1] = 1

        kernel_list = [kernel1, kernel2, kernel3, kernel4, kernel5, kernel6, kernel7, kernel8, kernel9, kernel10]
                
        self.initial_image = initial_image
        self.kernel_list = kernel_list
        self.ind = 0
        self.actual_kernel = self.kernel_list[self.ind]
        
        self.fig, self.axes = plt.subplots(1, 3, figsize=(15, 5))
        plt.subplots_adjust(bottom=0.25)
        self.ax_img1, self.ax_img2, self.ax_img3 = self.axes

        a = np.max(np.abs(self.actual_kernel))
        self.cm_k = self._custom_color_map(pow=1, nb_points=256, max=a)
        self.img1 = self.ax_img1.imshow(self.actual_kernel, cmap=self.cm_k, vmin=-a, vmax=a)
        self.fig.colorbar(self.img1, ax=self.ax_img1)

        self.img2 = self.ax_img2.imshow(self.initial_image, cmap='gray')
        self.fig.colorbar(self.img2, ax=self.ax_img2)

        conv_im = self._apply_convolution(self.initial_image, self.actual_kernel)
        b = np.max(np.abs(conv_im))
        self.cm_l = self._custom_color_map(pow=1, nb_points=256, max=1)
        self.img3 = self.ax_img3.imshow(conv_im, vmin=-b, vmax=b, cmap=self.cm_l)
        self.fig.colorbar(self.img3, ax=self.ax_img3)

        self.ax_img1.set_title('Kernel')
        self.ax_img2.set_title('Image + Noise')
        self.ax_img3.set_title('Convolution Result')

        self.ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
        self.slider = Slider(self.ax_slider, 'Noise Level', 0.0, 5, valinit=0.01)
        self.slider.on_changed(self._update)

        self.ax_button = plt.axes([0.8, 0.025, 0.1, 0.04])
        self.button = Button(self.ax_button, 'Change Kernel')
        self.button.on_clicked(self._charge_kernel)

    def _add_gaussian_noise(self, image, var=0.01):
        noisy_image = image + var * np.random.rand(*image.shape)
        return noisy_image

    def _apply_convolution(self, image, kernel):
        return correlate(image, kernel)

    def _custom_color_map(self, pow=1, nb_points=256, max=1):
        linear_ramp_d = np.flip(np.linspace(0, max, nb_points))
        linear_ramp_u = np.linspace(0, max, nb_points)
        powered_ramp_d = linear_ramp_d ** pow
        powered_ramp_u = linear_ramp_u ** pow

        colors = np.zeros((nb_points, 4))
        colors[:, 0] = 1
        colors[:, 1] = powered_ramp_d
        colors[:, 2] = powered_ramp_d
        colors[:, 3] = 1.0

        colors2 = np.zeros((nb_points, 4))
        colors2[:, 0] = powered_ramp_u
        colors2[:, 1] = powered_ramp_u
        colors2[:, 2] = 1
        colors2[:, 3] = 1.0
        colors_cat = np.vstack((colors2, colors))
        custom_cmap = mcolors.ListedColormap(colors_cat)
        return custom_cmap

    def _update(self, val):
        noise_level = self.slider.val
        noisy_image = self._add_gaussian_noise(self.initial_image, var=noise_level)
        self.img2.set_data(noisy_image)

        conv_im = self._apply_convolution(noisy_image, self.actual_kernel)
        b = np.max(np.abs(conv_im))
        self.img3.set_data(conv_im)
        self.img3.set_clim([-b, b])
        self.fig.canvas.draw_idle()

    def _charge_kernel(self, event):
        self.ind = (self.ind + 1) % len(self.kernel_list)
        self.actual_kernel = self.kernel_list[self.ind]

        a = np.max(np.abs(self.actual_kernel))
        self.img1.set_data(self.actual_kernel)
        self.img1.set_clim([-a, a])

        noise_level = self.slider.val
        noisy_image = self._add_gaussian_noise(self.initial_image, var=noise_level)
        self.img2.set_data(noisy_image)

        conv_im = self._apply_convolution(noisy_image, self.actual_kernel)
        b = np.max(np.abs(conv_im))
        self.img3.set_data(conv_im)
        self.img3.set_clim([-b, b])

        self.fig.canvas.draw_idle()

    def show(self):
        plt.show()