# Environments

One of Python's greatest strengths is the availability of community packages to tackle a wide variety of scientific/engineering tasks. This, however, leads to an unintended problem: **What happens when some of my packages require different versions of Python or other packages?**

For example, if we create our own package that requires [numpy](https://www.numpy.org/), but the developers are announcing some upcoming changes that might break the functionality of my code; how can we ensure that our package will continue to work if I update [numpy](https://www.numpy.org/) to work in another project in my computer?

##  Updating pip

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
