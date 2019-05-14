# dataPy: IDEs

Due to its popularity, python has several alternatives in terms of integrated developing environments. Throughout this bootcamp, we will go through three of the most commonly used open source options: [Spyder](https://www.spyder-ide.org/), [Jupyter](https://jupyter.org/), and [Atom](https://atom.io/).


<hr><hr>

##  Free and/or Open Source

Python's culture is based on open-source development and sharing of code. As such, several free and open source IDEs are readily available online for a variety of applications and programming tastes.

### [IDLE](https://docs.python.org/3/library/idle.html)

[IDLE](https://docs.python.org/3/library/idle.html) is an integrated development environment that comes packed with the standard python installation. It is a pretty basic but useful as it is a cross-platform tool to get python code running.

<img src="./media/idle.png" width="50%">


<hr>

### [Spyder](https://www.spyder-ide.org/)

A good option for people comfortable with [RStudio](https://www.rstudio.com/). This IDE mimics [R](https://www.r-project.org/)'s most popular coding environment and makes its functionalities available to Python programmers.

<img src="./media/spyder.png" width="50%">

####  Installation

To install [Spyder](https://www.spyder-ide.org/) in our [Anaconda](https://www.anaconda.com/) environment, we can do the following in the terminal:

```bash
source activate dataPy
conda install spyder
conda deactivate
```

Or we can install it from the [Anaconda](https://www.anaconda.com/) GUI.

####  Launching a Session

```bash
source activate dataPy
spyder
```

<hr>

### [Jupyter](https://jupyter.org/)

[Jupyter](https://jupyter.org/) is one of the most recent and famous IDEs created for Python. With this editor, we can generate interactive notebooks that can be shared with an [online viewer](https://nbviewer.jupyter.org/).

<hr>

### [Atom](https://atom.io/)

Developed by [github](https://www-github.com), [Atom](https://atom.io/) is one of the most versatile IDEs currently available.

<hr><hr>

##  Alternatives


### [PyCharm](https://www.jetbrains.com/pycharm/)

A comprehensive IDE for professional Python development. This IDE contains most of the common features found in computer science industry applications, such as: smart code completion, refractoring, profiling, code generation, code analysis, smart code navigation, etcetera.

<img src="./media/pycharm01.png" width="50%">
<img src="./media/pycharm02.png" width="50%">

<hr>

### [Sublime Text](https://www.sublimetext.com/)

A flexible cross-platform IDE with lots of customization options. Excellent for multi-language projects and fast development turnarounds.

<img src="./media/sublimeText.png" width="50%">

### [Eclipse (PyDev)](https://marketplace.eclipse.org/content/pydev-python-ide-eclipse)

For people used to coding in Eclipse, there's [PyDev](https://marketplace.eclipse.org/content/pydev-python-ide-eclipse), although it's not very popular amongst python developers.

<img src="./media/eclipse.jpg" width="50%">


<hr><hr>

##  Other Resources

* [Comprehensive Python IDEs list](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments)
