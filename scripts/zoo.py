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
zoo.head(10)

###############################################################################
# Filter and count
len(zoo)
zoo["animal"].count()
zoo.animal.count()

animalsList = list(zoo.animal)
animalsTypes = set(animalsList)

animalsTypes
zoo.animal.unique()


zoo["animal"].unique()

zoo[["animal", "water_need"]]
dir(zoo[["animal", "water_need"]])

help(pd.core.series.Series)

###############################################################################
# More filtering and stats
waterNeeded = zoo["water_need"]
print(f"""
Sum: {waterNeeded.sum()}
Max: {waterNeeded.min()}
Mean: {waterNeeded.mean()}
Median: {waterNeeded.median()}
""")
plt.hist(waterNeeded, color='blue', edgecolor='black', bins=int(180/5))


###############################################################################
# Mixed filtering and plotting
list(zoo.groupby("animal"))

waterGroupedMean = zoo.groupby("animal").mean()[["water_need"]]
waterGroupedMean
zoo.groupby("animal").mean()[["water_need"]]

help(waterGroupedSum.plot.bar())

waterGroupedSum = zoo.groupby("animal").sum().water_need
waterGroupedSum.plot.bar()


plt.close()
sns.barplot(
    x="animal", y="water_need", data=zoo,
    capsize=.2, linewidth=2.5, facecolor=(1, 1, 1, 0),
    errcolor=".2", edgecolor=".2", ci=99
)
plt.savefig('./images/zoo.png', dpi=500)
