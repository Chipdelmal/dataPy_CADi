# dataPy: Python 101 (part 1)

Let's get started with some python programming! For the introduction to the language, head to either of:
* https://www.onlinegdb.com/online_python_interpreter
* https://repl.it/

and type:

```python
print("Hello World!")
```

Now that we have gotten tradition out of the way, let's look at the fundamental types of the Python language, while doing some exercises.

<hr>

## Scalar Types

Scalar types are the most fundamental units of programming in python. They represent a single value of data and are the foundations of any program we will build throughout this bootcamp.

### Numeric

**Integers** and **floating-point numbers** are fundamental types in Python. Integers can store arbitrarily long numbers, and floats are, by default 64 bits (usually).

```python
iValue = 1384891
print(iValue ** 4)
```

Just as a note, in python 3.x we can perform the division between integers as we would in any math application (to get the result we would get in C, we need the **//** division operator).

```python
print(3/2)
print(3//2)
```

###  Strings

One of the least favorite subjects for programmers is string manipulation. Fortunately, python makes it easy to deal with these structures in everyday applications.

```python
a = "This is a string."
b = 'This is also a string.'

c = '''
This is a multiline
string.
'''
c.count("\n")
```

One thing to take into account, though, is that strings are an immutable type. This means that we can't change the contents of a string "in place".

```python
a = "This is a string"
a[5] = "x"
```

In python 3.x, strings are a sequence of unicode characters, so they can be accessed with indices (including slicing):

```python
list(a)
a[:3]
a[3:7]
a[3:]
```

We can also format strings in complex ways:

```python
template = '{0:.2f} {1:s} are worth US${2:d}'
template.format(4.5560, 'Argentine Pesos', 1)
```

###  Booleans

As expected, booleans are fundamental types in python (as in most other languages). These can take a value of **true** or **false** with one note: they are capitalized!

```python
print(True and False)
print(False or True)
```

One of the advantages of using booleans in python is that logic comparisons tend to be easy to read:

```python
print((True and False) or not (False or True))
```

Finally, an important thing to remember is that the operator **is** is different from the logical comparison **==**. The comparison **==** returns **true** when two variables contain the same information while **is** returns true when two variables are the same object (point towards the same location in memory).

```python
a = [1, 2, 3]
b = a
b is a


a = [1, 2, 3]
b = a.copy()
b is a
```

###  None

This is the **NULL** value in python. The **None** object exists as an instance in memory, and there is only one instance of it for every python program. One important thing to take into account is that we should always use the **is** operator to make comparisons to the **None** object:

```python
a = None
a is None
```

###  Dates and Times

In data wrangling, it is common to have to deal with date-time information. Python contains a built-in **datetime** module.

```python
from datetime import datetime, date, time
dt = datetime(2011, 10, 29, 20, 30, 21)
dt.day

datetime.date(2011, 10, 29)
datetime.strptime('20091031', '%Y%m%d')
dt.strftime('%m/%d/%Y %H:%M')
dt.replace(minute=0, second=0)
```


### Casting

Finally, we can change between types using **casts**:

```python
# Checking the tyopes
num_int = 123
num_str = "456"
type(num_int)
type(num_str)

# Changing string to integer
casted = int(num_str)
type(casted)

# Changing integer to string
casted = str(num_int)
type(casted)
```


<hr>

##  Control Flow

Control flow structures work in pretty much the same way as they do in other programming languages, although python does have some convenient shortcuts to make our lives easier.

###  if, elif, else

The most basic flow control structure: **if**; checks if some condition is met and takes an action accordingly.

```python
if x < 0:
  print("The number is negative.")
```
The accompanying **elif** (**else-if**) and **else** check more conditions, and perform actions if met, or if none are met.

```python
if x == 0:
  print("The number is zero")
elif x < 0:
  print("The number less than zero")
else:
  print("The number more than zero")
```

Additionally, we can use a ternary expression in the form: ```value = true-expr if condition else false-expr```, to make one-line comparisons.

```python
True if x > 0 else False
```

###  for loops

**For** loops iterate over collections of items (lists or tuples). We can use these loops in a traditional way:

```python
sum = 0
for i in range(0,10,1):
  sum = sum + i
  print(sum)
```

and we can access elements of lists in the same we would in other programming languages:

```python
numbers = ["One", "Two", "Three", "Four", "Five", "Six"]
numLen = len(numbers)
for i in range(numLen):
  print("Number " + str(i) + ": " + numbers[i])
```

However, the "pythonic" way to do this is by using the list itself as the iterator:

```python
numbers = ["One", "Two", "Three", "Four", "Five", "Six"]
for num in numbers:
  print(num)
```

Furthermore, we can traverse a list and use the index of the currently inspected element at the same time by taking advantage of the **enumerate** function:

```python
numbers = ["One", "Two", "Three", "Four", "Five", "Six"]
for num, name in enumerate(numbers, start=0):
  print("Number " + str(num) + ": " + name)
```

###  while loops

**While** loops are the most general ways to cycle a piece of code. In **while** loops, we set a condition to be met at the point we want to exit the loop:

```python
x=256
total = 0
while x > 0:
  if total > 500:
    break
  total = total + x
  x=x//2
```

###  pass

Used in blocks where no action is required:

```python
if x < 0:
  print('negative!')
elif x == 0:
  pass
else:
  print('positive!')
```

<hr>

##  Resources

* https://docs.scipy.org/doc/numpy-1.13.0/user/basics.types.html
* https://pyeda.readthedocs.io/en/latest/boolalg.html
* [McKinney, W. Python for Data Analysis - Data Wrangling with Pandas, Numpy and Python. (2018). ISBN-13: 1491957662](https://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1491957662/ref=asc_df_1491957662/?tag=hyprod-20&linkCode=df0&hvadid=312140868236&hvpos=1o1&hvnetw=g&hvrand=6431209822672155744&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9032076&hvtargid=pla-396828636441&psc=1)
* [Lutz, Mark, and David Ascher (2004). Learning Python. Learning. ISBN-13: 978-9351102014](http://books.google.com/books?hl=en&amp;lr=&amp;id=ftA0yk1Z92wC&amp;oi=fnd&amp;pg=PT16&amp;dq=Learning+Python&amp;ots=FzKMS8tOZC&amp;sig=2ZEqAODN6tUtsrczbwbqKeTSp60)
