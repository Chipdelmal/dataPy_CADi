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

###  while loops



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

###  range
