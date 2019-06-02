# dataPy: Python 102



## Files


```python
txtFile = open('../data/extracted/ioTest.csv','w')
txtFile.write("Testing output of text")
txtFile.close()
```

```python
import csv
with open("../data/extracted/tweepy/crispr.csv",) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row[0],row[1])
```

## OOP

Object-Oriented programming is a widespread coding paradigm. It is worth noting that we can code in Python without dwelling too much into **OOP** concepts (as we have been doing so far); however, having a basic understanding of these fundamentals can prove useful when moving into more complex applications.

The basic idea behind OOP is that we can define **classes** that have **attributes** and perform **actions**.

###  Basic Object-Oriented Concepts

* Class
* Instance
* Inheritance
* Composition
* Overloading

<hr>


<hr>

##  Resources
