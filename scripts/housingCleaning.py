###############################################################################
# "Housing data" example
###############################################################################
#  Objectives:
#
#  Source:
#   https://github.com/ageron/handson-ml/blob/master/02_end_to_end_machine_learning_project.ipynb
###############################################################################

# -----------------------------------------------------------------------------
# Instructions and other information
# -----------------------------------------------------------------------------
# Download the data from:
#   https://github.com/ageron/handson-ml/tree/master/datasets/housing
# Pandas:
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/
#   https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html
# CMaps:
#   https://matplotlib.org/tutorials/colors/colormaps.html
# -----------------------------------------------------------------------------

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Import required libraries
import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np
import scipy
import sklearn
import pandas as pd
from sklearn.impute import SimpleImputer
#%matplotlib inline

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Setup data path and read data
DATA_PATH = "../data/extracted/housing/"
DATA_FILE = "housing.csv"
FULL_PATH = DATA_PATH + DATA_FILE
data = pd.read_csv(FULL_PATH)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Get information about our dataframe
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isna.html
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html
data.isna()
data.isna().sum()

data["total_bedrooms"].isna()
data["total_bedrooms"].isna().sum()

data.dropna(subset=["total_bedrooms"])
data.drop("total_bedrooms", axis=1)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Imputing data
#   https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html
#   https://scikit-learn.org/stable/modules/impute.html
median = data["total_bedrooms"].median()
print(median)
data["total_bedrooms"].fillna(median, inplace=True)

# Create Imputer Object
imputer = SimpleImputer(strategy="median")
# Create a dataframe without the categorical column
housingNum = data.drop("ocean_proximity", axis=1)
# Fit the imputer to the new dataframe
imputer.fit(housingNum)
imputer.statistics_
housingNum.median().values
# Impute our dataframe (returns a numpu array)
impArray = imputer.transform(housingNum)
# Convert back into a dataframe
colNames=housingNum.columns
housingTr = pd.DataFrame(X,columns=colNames)
housingTr
