import numpy as np
import subprocess
import time
import os
from pathlib import Path
import shutil
import tempfile
from typing import List, Tuple

import bigfish.detection as detection
from bigfish.multistack import extract_cell, summarize_extraction_results
import bigfish.stack as stack


class DetectionPipeline:
    def spot_bigfish(
        self,
        rna: np.ndarray,
        voxel_size_nm=(300, 103, 103),
        object_radius_nm=(350, 150, 150),
        thresh=None
    ) -> np.ndarray:
        """Detect spots using bigfish.

        Args:
            rna (np.ndarray): 3 dimensional np.ndarray (z, w, h).
            voxel_size_nm (tuple, optional):  Defaults to (300, 103, 103).
            object_radius_nm (tuple, optional): Defaults to (350, 150, 150).
            thresh (float, optional). If None, automatic threshold selection is done.
            To get the range of thresholds see spot_big_fish_get_thresh.
            
        Returns:
            np.ndarray: n by 3 np.array, where n is the number of spots.
            For each triplet: first dimension is the number of z stack.
            Second and third dimension are the position in pixels.
        """
        spot_radius_px = detection.get_object_radius_pixel(
            voxel_size_nm=voxel_size_nm, object_radius_nm=object_radius_nm, ndim=len(object_radius_nm)
        )
        rna_log = stack.log_filter(rna, sigma=spot_radius_px)
        mask = detection.local_maximum_detection(rna_log, min_distance=spot_radius_px)
        if thresh is None:
            thresh = detection.automated_threshold_setting(rna_log, mask)
        spots, _ = detection.spots_thresholding(rna_log, mask, thresh)
        return spots
    
    def spot_big_fish_get_thresh_range(
        self,
        rna: np.ndarray,
        voxel_size_nm=(300, 103, 103),
        object_radius_nm=(350, 150, 150),
    )-> np.ndarray:
        """get possible thresholds for big fish.

        Args:
            rna (np.ndarray): 2D or 3D
            voxel_size_nm (tuple, optional): 2D or 3D, if rna is 2D, this also has to be 3D. Defaults to (300, 103, 103).
            spot_radius_nm (tuple, optional): 2D or 3D, if rna is 2D, this also has to be 3D. Defaults to (350, 150, 150).

        Returns:
            np.ndarray: thresholds.
        """
        thresholds, _ ,_  = detection.get_elbow_values(rna, voxel_size=voxel_size_nm, spot_radius=object_radius_nm)
        return thresholds


    def spot_big_fish_thresh_count_threshold(
        self,
        rna: np.ndarray,
        voxel_size_nm=(300, 103, 103),
        object_radius_nm=(350, 150, 150),
    ):
        thresholds, count_spots, threshold  = detection.get_elbow_values(rna, voxel_size=voxel_size_nm, spot_radius=object_radius_nm)
        return thresholds, count_spots, threshold
        
        
    def spot_ufish(self, file_data: str, target_dir: str) -> np.ndarray:
        """Launches a script in bash (env_activate_ufish) which itself
        calls a function det_spots that can run in the ufish environment.
        The function det_spots saves temporally a .npy file, the function
        spot_ufish reads it, outputs the numpy array with the coordinates
        of the detected spots (z,y,x) and finally erases the temp file.

        Args:
            file_data (str): single channel .tiff file containing the FISH
            image. Usually after being loaded the file, the images from each
            channels are splitted and saved in /Analysis/temp.
            Example file name:
            '../Analysis/temp/HEK_FISH.tiff'

            base_dir: the absolute path to the parent directory of src.    

            target_dir (str): suposing the Acquisition, Analysis, Code
            structure of the file, itarget_dir can be
            str(Path().resolve().parent / Path('Analysis/temp/detected_ufish.npy'))

        Raises:
            ImportError: When execution fails, it can't open the written
            file.

        Returns:
            np.ndarray: n by 3 np.array, where n is the number of spots.
            For each triplet: first dimension is the number of z stack.
            Second and third dimension are the position in pixels.
        """
        base_dir = Path('./')
        bash_script_path = "env_activate_ufish_v2.sh"        
        start_time = time.time()
        result = subprocess.run(
            ["bash", bash_script_path, file_data, target_dir, base_dir],
            capture_output=True,
            text=True,
        )
        print(result)
        end_time = time.time()
        print(f"Execution time {end_time - start_time:.2f} seconds.")

        if os.path.isfile(target_dir):
            spots_uf = np.load(target_dir)
            Path(target_dir).unlink()  # delete the temp file
            return spots_uf
        else:
            raise ImportError("The detection file from U fish was not generated !")    
