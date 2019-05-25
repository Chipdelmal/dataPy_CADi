# dataPy: Python 101 (part 2)

With the introductions out of the way, let's install Python in our systems and

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

##  Mutability

### Mutable


####  Lists

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

#### Immutable

```python
# Strings
strg = "Strings are immutable"
strg[0] = "Z"

# Tuples
tup = (1,2)
```

<hr>

### Functions

```python
def lstToStr(inList):
  converted = ",".join(str(e) for e in inList)
  return "[" + converted + "]"
```
<hr>
