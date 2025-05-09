# Cell segmentation with CellPose

In this course, we will see how to segment cells for spatial omics (in large 2D images) using CellPose.
We will explore CellPose parameters and different versions of CellPose

## Installation

Clone this repository.
In the repository directory, create a new virtual environnement:
```
conda env create -n cellposenv --python=3.11 
```

And activate the environment when it's done
```
conda activate cellposenv
```


Install the dependencies:
```
conda install cellpos.yaml
```

Finally, install in the src directory the version 3 of Cellpose:
```
pip install cellpose[distributed]==3.1.1.2 --target=src/cellpose3
```

## Data

Download datasets here:

(or use your own data)

## Usage

Open the `CellPose.ipynb` notebook
