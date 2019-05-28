###############################################################################
# "CRISPR" example
###############################################################################
#  Objectives:
#   To learn how to merge dataframes in pandas
#  Source:
#   https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
#   https://www.datacamp.com/community/tutorials/joining-dataframes-pandas
#   https://trends.google.com/trends/explore?geo=MX&q=crispr
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Import required libraries
%matplotlib inline
import pandas as pd

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Loading the US trends for CRISPR
data = pd.read_csv("../data/extracted/Trends/CRISPR.csv", header=1)
data.keys()
data.rename(columns={"Month": "month", 'crispr: (United States)': "US"},inplace=True)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Loading the worldwide trends for CRISPR
dataW = pd.read_csv("../data/extracted/Trends/CRISPRWorld.csv", header=1)
dataW.keys()
dataW.rename(columns={"Month": "month", 'CRISPR: (Worldwide)': "World"}, inplace=True)


pd.concat([data, dataW], axis=1)
dataFull = pd.merge(data, dataW, how="cross", on="month")
dataFull

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Loading the Mexican trends for CRISPR with a reduced timespan
dataM = pd.read_csv("../data/extracted/Trends/CRISPRMx.csv", header=1)
dataM.keys()
dataM.rename(columns={"Month": "month", 'crispr: (Mexico)': "Mx"}, inplace=True)
pd.merge(dataM, dataFull, how="left", on="month")
