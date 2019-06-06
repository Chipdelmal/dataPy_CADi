# -*- coding: utf-8 -*-

###############################################################################
# "NBA" example
###############################################################################
#  Objectives:
#   Another df.groupby example
#  Source:
#   https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html
#   https://www.geeksforgeeks.org/python-pandas-pivot/
#   https://www.geeksforgeeks.org/python-pandas-df-size-df-shape-and-df-ndim/
###############################################################################

# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.read_csv("../data/extracted/nba/nba.csv")

grouped = df.groupby('Team')
grouped.first()
grouped.get_group('Boston Celtics')

groupedDouble = df.groupby(['Team', 'Height'])
groupedDouble.head()
groupedDouble.first()

df.columns
df.pivot(index="Name", columns="Height", values="Salary")






# import numpy as np
# import pandas.util.testing as tm
# print(pd.__version__)
#
#
# tm.N = 3
# def unpivot(frame):
#     N, K = frame.shape
#     data = {
#         'value': frame.to_numpy().ravel('F'),
#         'variable': np.asarray(frame.columns).repeat(N),
#         'date': np.tile(np.asarray(frame.index), K)
#     }
#     return pd.DataFrame(data, columns=['date', 'variable', 'value'])
#
# df = unpivot(tm.makeTimeDataFrame())
# filter = (df['variable'] == 'A')
# df[filter]
#
# help(df.pivot)
# df.pivot(index="date", columns="variable", values="value")
