# -*- coding: utf-8 -*-

###############################################################################
# "Spyder Walk" example
###############################################################################
#  Objectives:
#   To test the Google Trends data retreival within Python
#  Sources:
#   https://www.geeksforgeeks.org/random-walk-implementation-python/
###############################################################################

# Import libraries
import numpy
import pylab
import random

# Number of steps and defining the array for them
n = 10000
(x, y) = (numpy.zeros(n), numpy.zeros(n))

# Random Walking
for i in range(1, n):
    val = random.randint(0, 3)
    if val == 0:
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif val == 1:
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif val == 2:
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    else:
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1


# Plotting the results
pylab.title("Random Walk ($n = " + str(n) + "$ steps)")
pylab.plot(x, y)
pylab.savefig("./images/spyderWalk.png", bbox_inches="tight", dpi=600)
pylab.show()
