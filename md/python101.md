# Python 101

##  Introduction

Python is currently one of the most widely used programming languages.

### Why is Python popular?

* Open source
* Easy to learn, yet comprehensive for complex tasks
  * Speed
  * Productivity
* Very powerful scripting language
  * Ideal for making prototypes
  * Ideal for data science
* Good code core packages
* Large community
  * Wide selection of third-party packages (pip)
  * Lots of online support for almost any kind of programming application


<hr>

##  Installation

<hr>

##  First Steps

For the introduction to the language, let's head to either of:
* https://www.onlinegdb.com/online_python_interpreter
* https://repl.it/

### Hello World!

```python
print("Hello World!")
```

### Functions

```python
def lstToStr(inList):
  converted = ",".join(str(e) for e in inList)
  return "[" + converted + "]"
```

### Types

```python
num = 10
strg = "Hello World!"
num = "test"
```
<hr>

##  Mutability



##### Mutable


######  Lists

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

##### Immutable

```python
# Strings
strg = "Strings are immutable"
strg[0] = "Z"

# Tuples
tup = (1,2)
```
