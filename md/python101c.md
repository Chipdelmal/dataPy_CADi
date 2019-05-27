# dataPy: Python 101 (part 3)

<hr>

## Useful functions for collections of data

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

### sorted

```python
sorted([7, 1, 2, 6, 0, 3, 2])
```

### zip

```python
seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
zipped = zip(seq1, seq2)
list(zipped)
```

### reverse

<hr>

## Importing Packages

<hr>

##  Resources

* [McKinney, W. Python for Data Analysis - Data Wrangling with Pandas, Numpy and Python. (2018). ISBN-13: 1491957662](https://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1491957662/ref=asc_df_1491957662/?tag=hyprod-20&linkCode=df0&hvadid=312140868236&hvpos=1o1&hvnetw=g&hvrand=6431209822672155744&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9032076&hvtargid=pla-396828636441&psc=1)
* [Lutz, Mark, and David Ascher (2004). Learning Python. Learning. ISBN-13: 978-9351102014](http://books.google.com/books?hl=en&amp;lr=&amp;id=ftA0yk1Z92wC&amp;oi=fnd&amp;pg=PT16&amp;dq=Learning+Python&amp;ots=FzKMS8tOZC&amp;sig=2ZEqAODN6tUtsrczbwbqKeTSp60)
