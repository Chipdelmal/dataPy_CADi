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

This is not a CS data structures course, nevertheless, it is important to understand how data is stored in python so that we can manipulate it as we desire.

### List and Slicing

```python
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

Same as in programming languages as Mathematica and R, we can "slice" elements of lists easily in python:

```python
# Getting elements through indices
a = [7, 1, 2, 6, 0, 3, 2]
a[2:4]
# Replacing elements
a[2:3] = [0,0]
# Getting elements from the end
a[-2]
```

####  Add, Remove and Combine

####  Sorting and Searching

### Dictionary

### Tuples

### Set

A set is, as its mathematic counterpart, an unordered collection of unique elements. It support operations such as union, intersection, difference, and symmetric difference. These structures are specially useful to check if an element has already been visited in a traverse algorithm, or to get the unique elements in a structure.

<hr>

## Files


<hr>

## Functions

```python
def sumTwoValues(a, b=0):
  return a + b
```

```python
def listToString(inList):
  converted = ",".join(str(e) for e in inList)
  return "[" + converted + "]"
```

Functions are regular objects in python, as such, we can do things like the following:

```python
import re
def remove_punctuation(value):
  return re.sub('[!#?]', '', value)

def clean_strings(strings, ops):
  result = []
  for value in strings:
    for function in ops:
      value = function(value)
    result.append(value)
  return result

states = ['   Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 'south   carolina##', 'West virginia?']
clean_ops = [str.strip, remove_punctuation, str.title]
clean_strings(states, clean_ops)
```
