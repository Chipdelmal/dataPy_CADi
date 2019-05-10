# Environments

Virtual environments attempt to solve a variety of problems that arise when working in several programming projects at the same time. In this section of our bootcamp we will go through some of these uses and we will setup the environment that we will be using for the rest of the workshop.

## What is an environment and why should I use one?

###  Packages "Hygene"

One of Python's greatest strengths is the availability of community packages to tackle a wide variety of scientific/engineering tasks. This, however, leads to an unintended problem: **What happens when some of my packages require different versions other packages? (or even different versions of Python)**

For example, if we create our own package that requires [numpy](https://www.numpy.org/), but the developers are announcing some upcoming changes that might break the functionality of my code; how can we ensure that our package will continue to work if I update [numpy](https://www.numpy.org/) to work in another project in my computer?

Environments solve this problem in an elegant way by providing "workspaces" within our system in which we can install/uninstall packages without affecting the dependencies of other projects we might be working on.

### Portability

Another problem environments address is the "shipping" of our code. This is: **How do I share my code with collaborators and users without them having to install and figure out packages dependencies by themselves?**

By creating a virtual environment, we are already

##  Getting started (updating pip)

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
