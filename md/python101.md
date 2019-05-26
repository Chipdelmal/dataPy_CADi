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


### Numeric

Integers and floating-point numbers are fundamental types in Python. Integers can store arbitrarily long numbers, and floats are

```python
iValue = 1384891
print(iValue ** 4)
```


```python
print(3/2)
print(3//2)
```

###  Strings

###  Booleans

###  None

###  Dates and Times

### Casting

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
