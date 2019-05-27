# dataPy: [Anaconda](https://www.anaconda.com/)

In this workshop, we will be using anaconda as our environment manager. The reason to prefer it over virtualenv is that it can be used with [R](https://www.r-project.org/) (which is also commonly used for data-analysis applications), and because it also provides a user interface, which makes it accessible for a wider audience.

[<img src="./media/anacondaBanner.png" width="100%">](https://www.anaconda.com/distribution/)

## Installing Anaconda

Anaconda does not come bundled with our python installation, so we have to head to the [download section of the project's website](https://www.anaconda.com/distribution/) and install it.


[<img src="./media/anacondaDownload.png" width="100%">](https://www.anaconda.com/distribution/)

Once we've installed it, we can move forward to creating the environment we will use throughout the bootcamp.

## Creating an environment

```bash
conda create -n dataPy python=3.7
```

To install from *yml* file:

```bash
conda env create -f dataPy.yml
```

## Installing packages on the environment

```bash
source activate dataPy
pip install pandas
pip install numpy
conda deactivate
```

## Adding the kernel to Jupyter/Atom (optional)

```bash
python -m ipykernel install --user --name dataPy
```


## Exporting an environment to a YML file

```bash
conda env export > dataPy.yml
```
