# -*- coding: utf-8 -*-

###############################################################################
# "Housing data (cleaning)" example
###############################################################################
#  Objectives:
#   Doing pandas dataframe manipulation to clean and create a categorical
#       variable encoding.
#  Sources:
#   https://github.com/ageron/handson-ml/blob/master/02_end_to_end_machine_learning_project.ipynb
#   https://github.com/ageron/handson-ml/tree/master/datasets/housing
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/
#   https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html
#   https://matplotlib.org/tutorials/colors/colormaps.html
#   http://contrib.scikit-learn.org/categorical-encoding/
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isna.html
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html
#   https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html
#   https://scikit-learn.org/stable/modules/impute.html
###############################################################################


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Import required libraries
# import matplotlib as plt
# import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.preprocessing import OneHotEncoder
%matplotlib inline

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Setup data path and read data
DATA_PATH = "../data/extracted/housing/"
DATA_FILE = "housing.csv"
FULL_PATH = DATA_PATH + DATA_FILE
data = pd.read_csv(FULL_PATH)
data.head()


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Get information about our dataframe
data.isna()
data.isna().sum()

data["total_bedrooms"].isna()
data["total_bedrooms"].isna().sum()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Droping NA's

# Drops rows with NA entries
# data.dropna(subset=["total_bedrooms"], inplace=True)

# Delete a column (axis=1)
# data.drop("total_bedrooms", axis=1, inplace=True)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Imputing data
#   median could be replaced with any other operation/value
#   (mean, min, max, etc)
median = data["total_bedrooms"].median()
print(median)
data["total_bedrooms"].fillna(median, inplace=False)
sum(data["total_bedrooms"] == median)


# Create a dataframe without the categorical column
housingNum = data.drop("ocean_proximity", axis=1)
# Create Imputer Object
imputer = SimpleImputer()
# imputer = IterativeImputer()
# Fit the imputer to the new dataframe
imputer.fit(housingNum)
# imputer.statistics_
# housingNum.median().values
# Impute our dataframe (returns a numpy array)
impArray = imputer.transform(housingNum)
# Convert back into a dataframe
colNames = housingNum.columns
housingTr = pd.DataFrame(impArray, columns=colNames)
housingTr

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Categorical
housingCat = data["ocean_proximity"]
housingCat.head(10)
data["ocean_proximity"].unique()

help(housingCat.factorize)
(housingCatEncoded, housingCatCategories) = housingCat.factorize()
encoder = OneHotEncoder(categories="auto", sparse=False)
housingCatT = housingCat.values.reshape(-1, 1)
housingCatOne = encoder.fit_transform(housingCatT)
housingCatOne

list(encoder.categories_[0])

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Put DF together
cleanDataset = housingTr
encodedDataframe = pd.DataFrame(
    housingCatOne,
    columns=list(encoder.categories_[0])
)
cleanDataset = cleanDataset.join(encodedDataframe)
cleanDataset.to_csv("../data/extracted/housing/cleanDataset.csv")
