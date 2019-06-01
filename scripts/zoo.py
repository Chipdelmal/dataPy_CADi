# -*- coding: utf-8 -*-

###############################################################################
# "Zoo" example
###############################################################################
#  Objectives:
#   Introduction to pandas, seaborn and matplotlib
#  Source:
#   https://data36.com/pandas-tutorial-2-aggregation-and-grouping/
#   https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0
#   https://data36.com/pandas-tutorial-1-basics-reading-data-files-dataframes-data-selection/
###############################################################################


###############################################################################
# Load libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
%matplotlib inline

###############################################################################
# Read dataset
zoo = pd.read_csv("../data/extracted/Zoo/zoo.csv")
zoo

###############################################################################
# Filter and count
zoo[["animal"]].count()
zoo.animal.count()
animalsList = list(zoo.animal)
animalsTypes = set(animalsList)

###############################################################################
# More filtering and stats
waterNeeded = zoo.water_need
waterNeeded.sum()
waterNeeded.min()
waterNeeded.max()
waterNeeded.mean()
waterNeeded.median()
plt.hist(waterNeeded, color='blue', edgecolor='black', bins=int(180/5))


###############################################################################
# Mixed filtering and plotting
waterGroupedMean = zoo.groupby("animal").mean()[["water_need"]]
zoo.groupby("animal").mean().water_need

waterGroupedSum = zoo.groupby("animal").mean().water_need
waterGroupedSum.plot.bar()

sns.barplot(
    x="animal", y="water_need", data=zoo,
    capsize=.2, linewidth=2.5, facecolor=(1, 1, 1, 0),
    errcolor=".2", edgecolor=".2"
)
plt.savefig('./images/zoo.png', dpi=500)
