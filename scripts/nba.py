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
