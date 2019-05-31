# dataPy: Advanced Python

<hr>

## Other Functions


### Timing Execution

```python
import math
import time
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



```python
# ----------------------------------------------------------------
import time
(timings, numbers) = ([],7500)
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

Compared to the traditional **for** loop implementation:

```python
import time
startTime = time.time()
###########################################################
list=[None]
for i in range(10000):
  list.append(math.factorial(i))
###########################################################
endTime = time.time()
print(endTime-startTime)
```






### Lambda Functions


<hr>

## Garbage Collection
