This page collects instructions, links and materials for the Day 5
# Day 5 (Friday, 16th of May)

## Keynote: 

> Auguste GENOVESIO

## Accelerating Image Processing with GPU-ready Libraries I & II

> Teacher: Stéphane RIGAUD  
> Helpers: Minh-Son Phan  

### Requirement & Install 

We will use a new python environment, we advise to use [miniforge](https://github.com/conda-forge/miniforge). Create one and activate it.

```bash
mamba create --name cle python=3.12 -y
mamba activate cle
```

Once activated, we will need the following package:
- pyclesperanto 
- dask
- zarr
- tifffiles
- jupyter
- pandas
- (optional) cupy

> [!NOTE]
> if you have an NVIDIA card, you can also install cupy

```bash
mamba install pyclesperanto dask zarr tifffiles jupyter pandas -y
```

And we can also install Napari for viewer
```bash
pip install 'napari[all]'
```

to quickly verify that your install is working correctly, you can run the following command. It should return a list of devices or raise an error if your install is not working.

```bash
python -c "import pyclesperanto as cle; print(cle.list_available_devices())"
```

> [!IMPORTANT]
> Additionnal package maybe required for MacOS and Linux:
> * __MacOS__ `mamba install -c conda-forge ocl_icd_wrapper_apple`
> * __LINUX__ `mamba install -c conda-forge ocl-icd-system`

### Data to download

[ToDownload and unzip at the root of the notebook](https://dl.pasteur.fr/fop/voUgjRtR/data.zip)
