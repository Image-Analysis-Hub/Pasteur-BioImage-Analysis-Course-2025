# Cell segmentation  on large images I: using CellPose

In this course, we will see how to segment cells for spatial omics (in large 2D images) using CellPose.
We will explore CellPose parameters and different versions of CellPose

## Installation

Clone this repository.
In the repository directory, create a new virtual environnement:
```
conda create -n cellposenv python=3.11 
```

And activate the environment when it's done
```
conda activate cellposenv
```


Install the dependencies:
```
pip install -r requirements.txt
```

Finally, install in the src directory the version 3 of Cellpose:
```
pip install 'cellpose[distributed]'==3.1.1.2 --target=src/cellpose3
```

## Data

Download datasets here: [https://dl.pasteur.fr/fop/arK1nNJz/data.zip ](https://dl.pasteur.fr/fop/arK1nNJz/data.zip)

(or use your own data)

## Usage

Open the `CellPose.ipynb` notebook


# RNA2seg: Cell segmentation in image-based spatial transcriptomics

In this course, we will apply cell segmentation to Image-Based Spatial Transcriptomic (IST) data. 
The segmentation task enables the association of each sequenced RNA to a cell, creating the RNA count matrix. The accuracy of segmentation in ST is therefore crucial.

We introduce RNA2seg, a versatile model that performs segmentation on image-based spatial transcriptomic data (Merscope, Xenium, CosMX). 
RNA2seg accounts for both different stains (DAPI, various cell boundaries) and RNA localization, enabling efficient segmentation regardless of cell boundary quality. 
Often, the quality of cell boundaries is variable and may be associated with different cellular subtypes.

## Installation

It is recommended to create a virtual environment before installing RNA2seg to isolate dependencies:

```bash
$ conda create --name rna2seg-env python=3.10
$ conda activate rna2seg-env
```

Then, install RNA2seg and its dependencies:

```bash
(rna2seg-env) $ pip install rna2seg
```

## Data

Download datasets [here](https://drive.google.com/file/d/1NGTglMnCTxW-oG4XV_8ffCQ9S2JKeAGk/view?usp=sharing).

You can also use your own data, provided it is formatted as a Zarr file.

## Usage

Open the `RNA2seg.ipynb` notebook.