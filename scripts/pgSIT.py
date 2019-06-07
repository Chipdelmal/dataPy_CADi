# -*- coding: utf-8 -*-

###############################################################################
# "pgSIT"
###############################################################################
#  Objectives:
#   To do an exercise on how to load and operate on multi-dimensional numpy
#       arrays.
#  Source:
#    https://docs.scipy.org/doc/numpy-1.13.0/reference/arrays.ndarray.html
###############################################################################

import glob
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

###############################################################################
# Define the experiment's path and constants
experimentPath = "/Users/sanchez.hmsc/Documents/GitHub/dataPy_CADi/data/extracted/pgSIT/"
sexID = "AF1"
skipColumns = 1
type = np.uint16

###############################################################################
# Loading files
sortedFilenames = sorted(
    glob.glob(
        experimentPath + "/" +
        sexID + "*.csv"
    )
)

###############################################################################
# Load a file to prime the shape of the 3D array
filename = sortedFilenames[0]
timeData = np.genfromtxt(
    filename,
    dtype=np.uint16,
    skip_header=True,
    delimiter=",",
    invalid_raise=False
)[:, skipColumns:]

###############################################################################
# Prime a 3D array
shp = timeData.shape
experimentSet = np.empty([len(sortedFilenames), shp[0], shp[1]], dtype=type)
experimentSet[0] = timeData

###############################################################################
# Fill up the array
for (i, filename) in enumerate(sortedFilenames[1:]):
    timeData = np.genfromtxt(
        filename,
        dtype=np.uint16,
        skip_header=True,
        delimiter=",",
        invalid_raise=False
    )[:, skipColumns:]
    experimentSet[i+1] = timeData

###############################################################################
# Do some stats and plot
stat = experimentSet.var(axis=0)
plt.plot(stat)
