# Download the data from:
#   https://github.com/ageron/handson-ml/tree/master/datasets/housing
# Pandas API:
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/

# Import required libraries
import matplotlib
import numpy
import pandas
import scipy
import sklearn
import pandas as pd

# Setup data path
DATA_PATH = "../data/extracted/housing/"
DATA_FILE = "housing.csv"
FULL_PATH = DATA_PATH + DATA_FILE

# Read the CSV file into a data frame
data = pd.read_csv(FULL_PATH)

# Get information about our dataframe
data.head(10)
data.info()
headers = list(data)
print(headers)

data["ocean_proximity"]
data["ocean_proximity"].value_counts()


data.describe()
