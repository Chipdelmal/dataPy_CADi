# dataPy: Python 101 (part 2)

For the second part of the Python introduction, let's install Python in our systems (or update it), along with Anaconda (which we will use later in the bootcamp). With our installations in place, we will explore some deeper concept we will require throughout the course.

<hr>

##  Installation

Head to the [python downloads website](https://www.python.org/downloads/), and download [version 3.7.3 installer for your operating system](https://www.python.org/downloads/release/python-373/) and follow the instructions.

Additionally, let's take some time to install [Anaconda for Python 3.7](https://www.anaconda.com/distribution/), which we will be using later during the bootcamp.

To check that our python distribution was correctly installed, let's run the following command in the terminal:

```bash
python --version
```

It should return **Python 3.7.x**.

<hr>

##  Data Structures

### Tuples

### List

```python
# Lists
lstA = [1, 2, 3, 4]
lstA[0] = 5
print(",".join(str(e) for e in lstA))
```

```python
lstB = lstA
lstA[0] = -1

print(
  "A: [" + ",".join(str(e) for e in lstA) + "] \n" +
  "B: [" + ",".join(str(e) for e in lstA) + "]"
)
```

####  Add and Remove

####  Combining

####  Sorting

####  Searching

####  Slicing

### Dictionary

### Set

<hr>

## Files
