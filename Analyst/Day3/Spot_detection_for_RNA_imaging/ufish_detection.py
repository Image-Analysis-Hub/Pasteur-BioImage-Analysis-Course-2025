import sys
from pathlib import Path
import numpy as np
from skimage import io
from ufish.api import UFish
import torch


def det_spots(file_data: str, target_dir: str):
    """
    Detect spots using Ufish in ufish environment.

    Inputs:
        file_data: string, address of the .tiff file containing the fish.
        target_dir: the absolute path of where to store the temp .npy file (Analysis/temp/detected_ufish.npy)
    Output:
        spots: n by 3 np.array, where n is the number of spots.
    For each triplet: first dimension is the number of z stack
                                      second and third dimension is the position in pixels.
    Saves as a tuple of size 3 :(z, y ,x) each spot in a .npy file.
    """
    # print(" INSIDE THE UFISH env")

    ufish = UFish()

    if torch.cuda.is_available():
        weitghs_dir = Path(__file__).parent.resolve() / "v1.0-alldata-ufish_c32.pth"
        ufish.load_weights(weights_path=weitghs_dir)
    else:
        ufish.load_weights()

    rna = io.imread(file_data)

    if torch.cuda.is_available():
        pred_spots, _ = ufish.predict(
            rna, batch_size=1
        )  # try to increase later or to free GPU memory
    else:
        pred_spots, _ = ufish.predict(rna)

    np.save(target_dir, pred_spots.to_numpy())


if __name__ == "__main__":
    file_data = sys.argv[1]
    target_file = sys.argv[2]
    det_spots(file_data, target_file)
