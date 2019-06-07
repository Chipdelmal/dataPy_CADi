# -*- coding: utf-8 -*-

###############################################################################
# "Comoros"
###############################################################################
#  Objectives:
#   To show an example of using a custom-made package to do numpy array
#       manipulations
#  Source:
#   https://docs.scipy.org/doc/numpy-1.13.0/reference/arrays.ndarray.html
###############################################################################

import MoNeT_MGDrivE as monet
colors = [
    "#090446", "#f20060", "#c6d8ff", "#ff28d4", "#7fff3a", "#7692ff"
]
cmaps = monet.generateAlphaColorMapFromColorArray(colors)
styleS = {
    "width": 0, "alpha": .85, "dpi": 1024, "legend": True,
    "aspect": .25, "colors": colors,
    "xRange": [0, 1000], "yRange": [0, 1000]
}


###############################################################################
# Comors Pre-Processing
###############################################################################

###############################################################################
# Define the experiment's path
path = "/Users/sanchez.hmsc/Documents/GitHub/dataPy_CADi/data/extracted/comoros/"

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
figB = monet.plotMeanGenotypeStack(aggData, styleS)
figB.get_axes()[0].set_xlim(styleS["xRange"][0], styleS["xRange"][1])
figB.get_axes()[0].set_ylim(styleS["yRange"][0], styleS["yRange"][1])

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

overlay = monet.plotGenotypeOverlayFromLandscape(
    geneSpatiotemporals,
    style={"aspect": 10, "cmap": cmaps},
    vmax=monet.maxAlleleInLandscape(
        geneSpatiotemporals["geneLandscape"]
    )
)
