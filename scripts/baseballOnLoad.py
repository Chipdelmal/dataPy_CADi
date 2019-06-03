# -*- coding: utf-8 -*-

###############################################################################
# "Baseball" example
###############################################################################
#  Objectives:
#  Source:
#   https://www.dataquest.io/blog/pandas-big-data/
#   https://towardsdatascience.com/why-and-how-to-use-pandas-with-large-data-9594dda2ea4c
#   https://data.world/dataquest/mlb-game-logs/workspace/data-dictionary
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.select_dtypes.html
#   https://docs.scipy.org/doc/numpy/reference/generated/numpy.iinfo.html
#   https://docs.scipy.org/doc/numpy/reference/generated/numpy.finfo.html
#   https://www.programiz.com/python-programming/methods/built-in/isinstance
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_numeric.html
#   https://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Import required libraries
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
%matplotlib inline


def mem_usage(pandas_obj):
    if isinstance(pandas_obj, pd.DataFrame):
        usage_b = pandas_obj.memory_usage(deep=True).sum()
    else:  # we assume if not a df it's a series
        usage_b = pandas_obj.memory_usage(deep=True)
    usage_mb = usage_b / 1024 ** 2  # convert bytes to megabytes
    return "{:03.2f} MB".format(usage_mb)


typesSpecsFile='../data/extracted/baseball/keysDict.pickle'

with open(typesSpecsFile, 'rb') as handle:
    dataTypes = pickle.load(handle)



dataSource = "../data/extracted/baseball/game_logs.csv"
optimized_gl = pd.read_csv(
    dataSource,
    dtype=dataTypes,
    parse_dates=['date'],
    infer_datetime_format=True,
    low_memory=False
)
print(mem_usage(optim))


optimized_gl['year'] = optimized_gl.date.dt.year
games_per_day = optimized_gl.pivot_table(index='year',columns='day_of_week',values='date',aggfunc=len)
games_per_day = games_per_day.divide(games_per_day.sum(axis=1),axis=0)
ax = games_per_day.plot(kind='area',stacked='true')
ax.legend(loc='upper right')
ax.set_ylim(0,1)
plt.show()


game_lengths = optimized_gl.pivot_table(index='year', values='length_minutes')
game_lengths.reset_index().plot.scatter('year','length_minutes')
plt.show()
