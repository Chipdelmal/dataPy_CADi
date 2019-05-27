# dataPy: Python 101 (part 3)

<hr>

## Useful functions for collections of data

### Comprehensions

```[expr for val in collection if condition]```

```python
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
[x.upper() for x in strings if len(x) > 2]
unique_lengths = {len(x) for x in strings}
loc_mapping = {val : index for index, val in enumerate(strings)}
```

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
