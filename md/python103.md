# dataPy: Advanced Python

<hr>

## Timing Execution

As in any other programming language, performance is important. This is specially true when dealing with large datasets.

```python
import time
import math
startTime = time.time()
###########################################################
dummy = [math.factorial(x) for x in range(10000)]
###########################################################
endTime = time.time()
print(endTime-startTime)
```

<hr>

##  Map

For people used to functional programming, Python's **map** function should be straightforward to apply a function over a collection of elements:

```python
# Defining a test function
def squareNumber(n):
  return n**2
# Mapping the function through a list
map(squareNumber, range(5000))
```

We can map a function over several data structures at the same time:

```python
def add_three_numbers(num1, num2, num3):
  return num1 + num2 + num3

l1 = [1, 2, 3, 4, 5]
l2 = [11, 12, 13, 14, 15]
l3 = [21, 22, 23, 24, 25]
map(add_three_numbers,l1,l2,l3)
```

And we can also use constant arguments in our functions with an auxiliary **lambda function**:

```python
def offset(n, constant=0):
  return n + constant

numbers = range(10)
map(lambda n: offset(n, constant=3), numbers)
```

Let's compare the performance of the **map** implementation versus the **list comprehension** and the **for loop**:


```python
# ----------------------------------------------------------------
import time
(timings, numbers) = ([],10000)
# Map ------------------------------------------------------------
startTime = time.time()
dummy = map(math.factorial,range(numbers))
timings.append(time.time()-startTime)
# Comprehensions -------------------------------------------------
startTime = time.time()
dummy = [math.factorial(x) for x in range(numbers)]
timings.append(time.time()-startTime)
# For ------------------------------------------------------------
startTime = time.time()
dummy = [None]
for i in range(numbers):
  dummy.append(math.factorial(i))
timings.append(time.time()-startTime)
# ----------------------------------------------------------------
print(timings)
```

In some situations, the time response of these implementations might be similar, but because of memory and differences in the functions it is worth knowing at least a couple of different ways to iterate and apply functions to elements in a collection.

<hr>

## Lambda (Anonymous) Functions

Lambda functions are a functions that are created without a name (hence, the "anonymous" part).

```python
g = lambda x: x*x*x
g(2)
```

These can be combined with other functional programming concepts such as **maps**, **filters**

```python
li = range(10, 50, 5)
op = map(lambda x: x + 10 , li)
print(list(op))

filtered = filter(lambda x: (x%2 != 0) , li)
print(list(filtered))
```

<hr>

## Garbage Collection and Memory Management

Python does not require tracking of pointers and manual memory management, insted it realies on a [garbage collector](https://docs.python.org/3.6/library/gc.html) that takes care of most of those duties. On top of this, python manages the creation of common objects (such as indices) so that there's no additional overhead for objects that are created often (such as int objects with value of 1 or 0).

```python
# For common integers, python creates one object and
#   assigns multiple references to it.
a = 1
b = 1
a is b

# If the ints are too long they are probably not indices,
#   so python creates another object.
a = 100000
b = 100000
a is b
```

Variables within a scope (such as a function) the references created within that scope are destroyed:

```python
import sys

foo = []
print(sys.getrefcount(foo))

def bar(a):
    print(sys.getrefcount(a))

bar(foo)
print(sys.getrefcount(foo))
```

Detecting, and deleting circular references requires calling the garbage collector. The [garbage collector](https://docs.python.org/3.6/library/gc.html) can be manipulated manually through its [API](https://docs.python.org/3.6/library/gc.html):

```python
import gc

print("Garbage collection thresholds:", gc.get_threshold())
collected = gc.collect()
print("Garbage collector: collected", "%d objects." % collected)
```

Python calls the garbage collection automatically based on time, or events.

<hr>

##  Resources

* https://howchoo.com/g/mtc4ntzkngi/understand-the-map-function-in-python
* https://stackoverflow.com/questions/49301880/pass-several-arguments-to-function-from-map
* https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
* https://rushter.com/blog/python-garbage-collector/
* https://www.geeksforgeeks.org/garbage-collection-python/
* https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/
* http://book.pythontips.com/en/latest/map_filter.html
