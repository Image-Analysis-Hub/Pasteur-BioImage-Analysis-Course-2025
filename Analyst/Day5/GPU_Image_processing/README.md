# Accelerating Image Processing with GPU-ready Libraries I & II

> Teacher: Stéphane RIGAUD  
> Helpers: Minh-Son Phan  

### Requirement & Install 

We will use a new python environment, we advise to use [miniforge](https://github.com/conda-forge/miniforge). Create one and activate it.

```bash
conda create --name cle python=3.12 -y
conda activate cle
```

Once activated, we will need the following package:
- pyclesperanto 
- dask
- zarr
- scikit-image
- jupyter
- pandas
- (optional) cupy

> [!NOTE]
> if you have an NVIDIA card, you can also install cupy

```bash
conda install pyclesperanto dask zarr jupyter pandas scikit-image -y
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
> * __MacOS__ `conda install -c conda-forge ocl_icd_wrapper_apple`
> * __LINUX__ `conda install -c conda-forge ocl-icd-system`

### Data to download

[To Download and unzip at the root of the notebook](https://dl.pasteur.fr/fop/voUgjRtR/data.zip)


## Bonus - Napari Assistant

[Napari assistant](https://github.com/haesleinhuepf/napari-assistant) for quick image processing with interface

For full usage, we rely on the [devbio-napari](https://github.com/haesleinhuepf/devbio-napari) package
```
mamba create --name devbio python=3.11 devbio-napari pyqt -c conda-forge -y
```

Update pyclesperanto to the latest version

```
pip install pyclesperanto -U
```

Start Napari-Assistant
```
naparia
```