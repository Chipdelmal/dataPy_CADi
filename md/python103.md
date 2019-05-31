# dataPy: Advanced Python

<hr>

## Other Functions


### Timing Execution

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

###  Map

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


### Lambda Functions



<hr>

## Garbage Collection

<hr>

##  Resources

* https://howchoo.com/g/mtc4ntzkngi/understand-the-map-function-in-python
* https://stackoverflow.com/questions/49301880/pass-several-arguments-to-function-from-map
* https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
