
# https://tomaugspurger.github.io/dplry-pandas.html
# https://github.com/hadley/nycflights13/blob/master/data-raw/airports.csv
# https://github.com/rich-iannone/so-many-pyspark-examples/blob/master/data-files/nycflights13.csv

# Import required libraries
%matplotlib inline
import pandas as pd
import numpy as np

flights = pd.read_csv("../data/Extracted/Flights/nycflights13.csv")
flights.shape
flights.head()

flights.query("month == 1 & day == 1")
flights[(flights.month == 1) & (flights.day == 1)]
flights.iloc[2:9]
flights.sort_values(['year', 'month', 'day'])
flights[['year', 'month', 'day']]
flights.tailnum.unique()
flights[['origin', 'dest']].drop_duplicates()
flights['gain'] = flights.arr_delay - flights.dep_delay
flights['speed'] = flights.distance / flights.air_time * 60
flights.dep_delay.mean()
flights.loc[np.random.choice(flights.index, 10)]
planes = flights.groupby("tailnum")
delay = planes.agg({"year": "count",
                    "distance": "mean",
                    "arr_delay": "mean"})
delay.query("year > 20 & distance < 2000")
daily = flights.groupby(['year', 'month', 'day'])
per_day = daily['distance'].count()
per_month = per_day.groupby(level=['year', 'month']).sum()
(
flights.groupby(['year', 'month', 'day'])
    [['arr_delay', 'dep_delay']]
    .mean()
    .query('arr_delay > 30 | dep_delay > 30')
)
