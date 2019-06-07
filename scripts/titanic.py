# -*- coding: utf-8 -*-

###############################################################################
# "Titanic" Encoder
###############################################################################
#  Objectives:
#   To create a "one-hot" encoder for the titanic dataset
#  Source:
#   https://jorisvandenbossche.github.io/blog/2017/11/20/categorical-encoder/
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html
###############################################################################

#############################################################################
# Import libraries
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

#############################################################################
# Load dataset from an online source
dataURL = "https://raw.githubusercontent.com/amueller/scipy-2017-sklearn/master/notebooks/datasets/titanic3.csv"
titanic = pd.read_csv(dataURL)

#############################################################################
# Drop rows with NA's from the dataset
titanic = titanic[['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked', 'survived']].dropna()
titanic.head()

#############################################################################
# Create a "one-hot" encoder with the dataset
encoder = OneHotEncoder(sparse=False)
encoder.fit_transform(titanic[['sex', 'embarked']])
print(encoder.categories_)


print(encoder)
