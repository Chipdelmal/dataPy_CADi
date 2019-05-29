# dataPy: Python 101 (part 3)

<hr>

## Importing Packages

In contrast to languages like C, in which we have to compile the libraries and link them to our compiler, it is fairly easy to both install, and run packages in Python. To install, it is common to use the **pip** package manager:

```bash
pip install numpy
```

### Installing PIP

There's a couple of ways to install pip, so let's first check if we already have it running in our computers:

```bash
pip --version
```

If it is not installed, let's install it by following the next steps (this guide is for MacOS/Linux, but a guide for windows computers can be found in [this link](https://projects.raspberrypi.org/en/projects/using-pip-on-windows)):


```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

Before moving on, let's make sure we are running the latest version by upgrading it:

```bash
# On Unix
pip install -U pip
# On Windows
python -m pip install -U pip
```

We are set! With this, we should be able to install and run packages with our Python distribution easily!

### Using PIP

With pip installed, let's install pandas!

```bash
pip install pandas
```

And list the packages that are currently installed in our system:

```bash
pip list
```

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


<hr>

## Useful functions for collections of data

In addition to the operations we've seen so far, there are some other common functions that are used

### Comprehensions

Comprehensions are one of the most beloved features in python. With them, we can process the elements of a list, tuple or dictionary and return a processed version of their elements. The general structure for comprehensions is:

```python
# Returning a list
[expr for val in collection if condition]
# Returning a tuple
(expr for val in collection if condition)
# Returning a dictionary
{key: value for val in collection if condition}
```

We can, for example, take a list of numbers square them and return a list in a single, clean, line of code:

```python
exList = [1, 2, 3, 4, 5, 6]
[i ** 2 for i in exList]
```

Extending the idea, we can calculate and return the squared value only of the even numbers:

```python
[i ** 2 for i in exList if i % 2 == 0]
```

At first, comprehensions might not look all that useful, but they can be used in very powerful ways:

```python
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
[x.upper() for x in strings if len(x) > 2]
```

And we can use them to generate dictionaries too:

```python
unique_lengths = {len(x) for x in strings}
loc_mapping = {val : index for index, val in enumerate(strings)}
```

As a final note, it is worth noting that list comprehensions usually run faster than their traditionally typed counterparts.

### enumerate

It is a common practice when iterating through elements of a sequence to keep track of the index of the current item:

```python
lst = ["car", "apple", "book"]
for (i, val) in enumerate(lst):
  print(str(i) + " : " + val)
```

### sorted and reverse

Sorting lists is also easy in python:

```python
a = [7, 1, 2, 6, 0, 3, 2]
sorted([7, 1, 2, 6, 0, 3, 2])
a.sort()
```

And reversing them is just as easy:

```python
a.reverse()
```

### zip

The **zip** operation can be thought of a **transpose** operation in mathematics (and mathematica programming). It combines the elements of two collections and returns them element-wise:

```python
seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
zipped = zip(seq1, seq2)
list(zipped)
```

<hr>

##  Resources

* [McKinney, W. Python for Data Analysis - Data Wrangling with Pandas, Numpy and Python. (2018). ISBN-13: 1491957662](https://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1491957662/ref=asc_df_1491957662/?tag=hyprod-20&linkCode=df0&hvadid=312140868236&hvpos=1o1&hvnetw=g&hvrand=6431209822672155744&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9032076&hvtargid=pla-396828636441&psc=1)
* [Lutz, Mark, and David Ascher (2004). Learning Python. Learning. ISBN-13: 978-9351102014](http://books.google.com/books?hl=en&amp;lr=&amp;id=ftA0yk1Z92wC&amp;oi=fnd&amp;pg=PT16&amp;dq=Learning+Python&amp;ots=FzKMS8tOZC&amp;sig=2ZEqAODN6tUtsrczbwbqKeTSp60)
