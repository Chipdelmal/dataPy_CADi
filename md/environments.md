# Environments



Updating on MacOs and Linux:

```bash
pip install -U pip
```


Updating on Windows:

```bash
python -m pip install -U pip
```

##  [virtualenv](https://virtualenv.pypa.io/en/latest/)

##  [Anaconda](https://www.anaconda.com/)

### Creating an environment

```bash
conda create -n DataStructures python=3.7
```

To install from *yml* file:

```bash
conda env create -f dataPy.yml
```


### Installing packages on the environment

```bash
source activate dataPy
pip install pandas
pip install numpy
conda deactivate
```

### Adding the kernel to Jupyter/Atom (optional)

```bash
python -m ipykernel install --user --name dataPy
```
