import MoNeT_MGDrivE as monet

###############################################################################
# Comors Pre-Processing
###############################################################################

###############################################################################
# Define the experiment's path
path = "/Users/sanchez.hmsc/Documents/GitHub/dataPy_CADi/data/extracted/Comoros/"

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
