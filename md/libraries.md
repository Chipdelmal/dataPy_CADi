# dataPy: Libraries

One of the main features of Python is the availability of community libraries readily available. Unlike other languages and platforms (such as R or Matlab), which are more focused on certain applications, Python spans a wide range of applications which include:

* Machine Learning: [pyTorch](https://pytorch.org/), [TensorFlow](https://www.tensorflow.org/), [SciKit learn](https://scikit-learn.org/stable/)
* Data Analysis: [pandas](https://pandas.pydata.org/), [Numpy](https://www.numpy.org/), [Matplotlib](https://matplotlib.org/)
* Computer Vision: [open-cv](https://pypi.org/project/opencv-python/)
* General Science: [scipy](https://www.scipy.org/), [StatsModels](https://www.statsmodels.org/stable/index.html)
* Biology: [Biopython](https://biopython.org/)

[<img src="./media/tensorFlow.png" width="100%">](https://www.tensorflow.org/)

<hr>

##  Installing Libraries

By far, the easiest and most common way to install Python packages is through [Pypi](https://pypi.org/), although they can be added to the Python path manually (something we will not cover in this course).

### [Pypi](./pypi.md)

[<img src="./media/pypi.png" width="100%">](https://pypi.org/)

### Github installation

It is also possible to install packages from github through **pip** by following this pattern (assuming the repo has a **setup.py** file):

```bash
pip install git+https://github.com/myuser/foo.git@v123
```
