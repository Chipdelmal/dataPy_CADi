# -*- coding: utf-8 -*-

###############################################################################
# "Baseball" example
###############################################################################
#  Objectives:
#   To look at a more practical way to optimize the memory use in pandas.
#  Source:
#   https://www.dataquest.io/blog/pandas-big-data/
#   https://towardsdatascience.com/why-and-how-to-use-pandas-with-large-data-9594dda2ea4c
#   https://data.world/dataquest/mlb-game-logs/workspace/data-dictionary
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.select_dtypes.html
#   https://docs.scipy.org/doc/numpy/reference/generated/numpy.iinfo.html
#   https://docs.scipy.org/doc/numpy/reference/generated/numpy.finfo.html
#   https://www.programiz.com/python-programming/methods/built-in/isinstance
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_numeric.html
#   http://acepor.github.io/2017/08/03/using-chunksize/
###############################################################################

###############################################################################
# Import required libraries
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import baseballAux as aux
%matplotlib inline


###############################################################################
# Defining data sources types
DATA_TYPES_SOURCE = '../data/extracted/baseball/keysDict.pickle'
DATA_PATH = "../data/extracted/baseball/game_logs.csv"

###############################################################################
# Loading the data types as defined in the previous exercise
with open(DATA_TYPES_SOURCE, 'rb') as handle:
    dataTypes = pickle.load(handle)
print(dataTypes)

###############################################################################
# Loading the dataset and doing the data optimization "on the fly"
optimized_gl = pd.read_csv(
    DATA_PATH,
    dtype=dataTypes,
    parse_dates=['date'],
    infer_datetime_format=True,
    low_memory=True
)
print(aux.mem_usage(optimized_gl))

###############################################################################
# Doing some plots on the ratio of games per day
optimized_gl['year'] = optimized_gl.date.dt.year
games_per_day = optimized_gl.pivot_table(
    index='year', columns='day_of_week',
    values='date', aggfunc=len
)
games_per_day = games_per_day.divide(games_per_day.sum(axis=1), axis=0)
ax = games_per_day.plot(kind='area', stacked='true')
ax.legend(loc='upper right')
ax.set_ylim(0, 1)
plt.show()
#plt.close()


###############################################################################
# Loading the dataset by chunks
optimized_gl = pd.read_csv(
    DATA_PATH,
    dtype=dataTypes,
    parse_dates=['date'],
    infer_datetime_format=True,
    low_memory=False,
    chunksize=5000
)
df = pd.DataFrame()
for gm_chunk in optimized_gl:
    df = pd.concat([df, gm_chunk])
    print(len(gm_chunk))
df.head()


###############################################################################
# Follow up: filter the loaded dataset to contain only: date and day of
#   the week and export to a CSV file
#   (http://acepor.github.io/2017/08/03/using-chunksize/)
