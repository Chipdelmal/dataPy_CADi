# https://docs.scipy.org/doc/numpy-1.13.0/reference/arrays.ndarray.html

import numpy as np
import glob
import MoNeT_MGDrivE as monet

###############################################################################
# Comors Pre-Processing
###############################################################################

###############################################################################
# Define the experiment's path
path = "/Users/sanchez.hmsc/Documents/GitHub/dataPy_CADi/data/extracted/pgSIT/"

###############################################################################
# Get the filenames lists
filenames = monet.readExperimentFilenames(path)
# Load a single node (Auxiliary function)
nodeIndex = 0
nodeData = monet.loadNodeData(
    filenames.get("male")[nodeIndex],
    filenames.get("female")[nodeIndex],
    dataType=float
)

###############################################################################
# Define the genotype aggregation function
aggregationDictionary = monet.autoGenerateGenotypesDictionary(
    ["W", "H", "R", "B"],
    nodeData["genotypes"]
)

###############################################################################
# Aggregate the whole landscape into one array
landscapeSumData = monet.sumLandscapePopulationsFromFiles(
    filenames,
    male=True,
    female=True,
    dataType=float
)

###############################################################################
# Aggregate the genotypes of a population
aggData = monet.aggregateGenotypesInNode(
    landscapeSumData,
    aggregationDictionary
)

###############################################################################
# Load the population dynamics data of the whole landscape
landscapeData = monet.loadLandscapeData(filenames, dataType=float)
aggregatedNodesData = monet.aggregateGenotypesInLandscape(
    landscapeData,
    aggregationDictionary
)
aggregatedNodesData["landscape"]
###############################################################################
# Calculate the gene dynamics over the whole landscape
geneSpatiotemporals = monet.getGenotypeArraysFromLandscape(
    aggregatedNodesData
)


###############################################################################
###############################################################################
###############################################################################

experimentPath = path
sexID = "ADM"
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

experimentSet.mean(axis=0)
