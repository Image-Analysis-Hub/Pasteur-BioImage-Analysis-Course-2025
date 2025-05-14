
# Workshop: Introduction to the SpatialData framework

In this workshop we will introduce the SpatialData framework, which is designed to handle and analyze diverse image data. While the framework is primarily focused on spatial omics data, it can also be applied to other types of image data.

The workshop will cover the following topics:
- **Introduction to SpatialData**: Overview of the framework and its capabilities.
- **Data handling**: How to load and manipulate spatial omics data using SpatialData.
- **Data visualization**: Techniques for visualizing spatial omics data.
- **Multimodal data integration**: How to register and integrate different modalities of image data.


## Practical setup

### Conda environment

Create a conda environment with the packages required for this workshop. This can be done by running the following command in your terminal (after navigating to the `spatialdata` directory):

```bash
conda env create -f environment.yml
```

Activate the environment with:

```bash
conda activate spatialdata
```

### Jupyter Notebook

To run the Jupyter notebooks, you can use the following command in your terminal to start the Jupyter server:

```bash
jupyterlab
```

### Downloading the data

1. Activate the environment as explained above
    ```bash
    conda activate spatialdata
    ```
2. Run the following command to download the data
    ```bash
    # download the raw data
    python download.py --data_dir data raw visium
    python download.py --data_dir data raw visium_hd
    python download.py --data_dir data raw xenium

    # download some already processed data
    python download.py --data_dir data zarr merfish

    # for the multimodality integration example, download the following datasets
    python download.py --data_dir data raw xenium_multimodal
    python download.py --data_dir data raw visium_multimodal
    ```

## Acknowledgements

This workshop is based on the work of the SpatialData team and has been almost entirely taken from https://github.com/PMBio/spatialdata-workshops. Thank you for making these materials available to the community!
