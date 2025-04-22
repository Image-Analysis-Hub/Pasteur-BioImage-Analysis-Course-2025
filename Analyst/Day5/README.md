This page collects instructions, links and materials for the Day 5
# Day 5 (Friday, 16th of May)

## Keynote: 

> Auguste GENOVESIO

## Accelerating Image Processing with GPU-ready Libraries I & II

> Teacher: Stéphane RIGAUD  
> Helpers: tbc  

### Requirement & Install

We will use a new python environment, we advise to use [miniforge](). Create one and activate it.

```bash
mamba create --name cle python=3.11 -y
mamba activate cle
```

Once activated, we will need the following package:
- pyclesperanto 
- dask
- tifffiles
- jupyter
- matplotlib
- (optional) cupy

> [NOTE]
> if you have an NVIDIA card, you can also install cupy

```bash
mamba install pyclesperanto dask tiffiles jupyter matplotlib -y
```

to quickly verify that your install is working correctly, you can run the following command. It should return a list of processors or raise an error if your install is not working.

```bash
python -c "import pyclesperanto as cle; print(cle.list_available_devices())"
```

### Presentation & Practicals

#### Introduction to GPUs

#### Image Processing using GPUs

#### Custom Kernel execution

#### Multi-GPU Tile distribution

#### Benchmarking