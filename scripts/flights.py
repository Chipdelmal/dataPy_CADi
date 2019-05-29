###############################################################################
# "Flights data" example
###############################################################################
#  Objectives:
#   To learn some of the most common operations used in pandas
#  Source:
#   https://tomaugspurger.github.io/dplry-pandas.html
###############################################################################
# Instructions and other information
# -----------------------------------------------------------------------------
# Sources:
#   https://github.com/hadley/nycflights13/blob/master/data-raw/airports.csv
#   https://github.com/rich-iannone/so-many-pyspark-examples/blob/master/data-files/nycflights13.csv
###############################################################################

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Import required libraries
import pandas as pd
import numpy as np

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Read data
flights = pd.read_csv("../data/Extracted/Flights/nycflights13.csv")
flights.shape
flights.head()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Querying with specific constrains
flights.query("month == 1 & day == 1")
flights[(flights.month == 1) & (flights.day == 1)]

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Querying by location
flights.iloc[2:9]

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Sort by key
flights.sort_values(['year', 'month', 'day'])
flights[['year', 'month', 'day']]

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Getting the unique elements in a column (categories)
flights.tailnum.unique()
flights[['origin', 'dest']].drop_duplicates()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Adding categories
flights['gain'] = flights.arr_delay - flights.dep_delay
flights['speed'] = flights.distance / flights.air_time * 60

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Getting basic statistics
flights.dep_delay.mean()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Random sampling
selection = np.random.choice(flights.index, 10)
flights.loc[selection]

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Aggregated statistics
planes = flights.groupby("tailnum")
delay = planes.agg({
    "year": "count",
    "distance": "median",
    "arr_delay": "mean"
})
delay.query("year > 20 & distance < 2000")

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Aggregated statistics
daily = flights.groupby(['year', 'month', 'day'])
per_day = daily['distance'].count()
per_month = per_day.groupby(level=['year', 'month']).sum()
(
    flights.groupby(['year', 'month', 'day'])
    [['arr_delay', 'dep_delay']]
    .mean()
    .query('arr_delay > 30 | dep_delay > 30')
)
