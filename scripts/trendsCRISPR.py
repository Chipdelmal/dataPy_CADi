# https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
# https://www.datacamp.com/community/tutorials/joining-dataframes-pandas

%matplotlib inline
import pandas as pd


data = pd.read_csv("../data/extracted/Trends/CRISPR.csv", header=1)
data.keys()
data.rename(columns={"Month": "month", 'crispr: (United States)': "US"},inplace=True)

dataW = pd.read_csv("../data/extracted/Trends/CRISPRWorld.csv", header=1)
dataW.keys()
dataW.rename(columns={"Month": "month", 'CRISPR: (Worldwide)': "World"}, inplace=True)


pd.concat([data, dataW], axis=1)
pd.merge(data, dataW, how="inner", on="month")
