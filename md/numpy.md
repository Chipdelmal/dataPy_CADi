# dataPy: [numpy](https://www.numpy.org/)

[Numpy](https://www.numpy.org/) is a really powerful package that allows fast scientific computing in [python](https://www.python.org/). It allows the creation and efficient manipulation of multidimensional arrays of data, and it also provides the mathematical functions to operate upon them. [Numpy](https://www.numpy.org/) is usually installed as part of the scipy distribution, which adds functionality that makes it comparable to matlab in terms of coding and operations (both: [matlab](https://www.mathworks.com/products/matlab.html) and [numpy](https://www.numpy.org/) rely on [BLAS](http://www.netlib.org/blas/) and [LAPACK](http://www.netlib.org/lapack/) for efficient linear algebra computations).

<img src="./media/numpyCasting.png" width="100%">

## Limitations

The major limitation of [numpy](https://www.numpy.org/) is that it requires data to be homogeneous in type (integers or floats), and that arrays are not flexible in terms of growing or shrinking. This is because [numpy](https://www.numpy.org/) maintains information in contiguous blocks of memory, so adding/deleting rows or columns implies moving the location of the whole array.

## When to use [numpy](https://www.numpy.org/)

Whenever we have layers of homogeneously-typed data that are gonna remain consistent in shape across arrays, we should use [numpy](https://www.numpy.org/) for the operations. This might sound like a pretty strict requirement, but it's actually pretty common in operations such as linear algebra, image processing, spatial analysis, signal processing, amongst others.

[<img src="./media/array.png" width="100%">](https://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/)

For a more detailed explanation of how Python handles memory click on the image, which has the reference to an interesting [article](https://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/).

<hr>

## Exercises

### [Exercise 1: CRISPR Spread](../scripts/comoros.py)

In this example, we will use the [MoNeT_MGDrivE](https://pypi.org/project/MoNeT-MGDrivE/) package to show how libraries can be built with numpy to manipulate homogeneously dimensional data.

[<img src="./media/heat.png" width="100%">](../scripts/comoros.py)

### [Exercise 2: pgSIT](../scripts/pgSIT.py)

This exercise shows how loading files with time series data into numpy works, and how to make use of it's multidimensional statistical operations.

[<img src="./media/pgSIT.png" width="50%">](../scripts/pgSIT.py)

<hr>

##  References

* https://www.numpy.org/devdocs/user/quickstart.html
* https://en.wikipedia.org/wiki/NumPy
