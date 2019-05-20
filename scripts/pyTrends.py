# https://brohrer.github.io/dataframe_indexing.html
# https://github.com/GeneralMills/pytrends
# https://towardsdatascience.com/heartbreak-monday-blues-and-pytrends-f1a398591a79
# https://data36.com/pandas-tutorial-2-aggregation-and-grouping/

import datetime
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
import pytrends
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)

kw_list = ["Blockchain"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')

# Interest Over Time
interest_over_time_df = pytrends.interest_over_time()
#interest_over_time_df.loc['2017-10-26']
print(interest_over_time_df.head())

# Interest by Region
interest_by_region_df = pytrends.interest_by_region()
print(interest_by_region_df.head())

# Related Queries, returns a dictionary of dataframes
related_queries_dict = pytrends.related_queries()
print(related_queries_dict)

# Get Google Hot Trends data
trending_searches_df = pytrends.trending_searches()
print(trending_searches_df.head())

# Get Google Top Charts
top_charts_df = pytrends.top_charts(cid='actors', date=201611)
print(top_charts_df.head())

# Get Google Keyword Suggestions
suggestions_dict = pytrends.suggestions(keyword='pizza')
print(suggestions_dict)






kw_list = ["how to breakup"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')

# Interest Over Time
trends = pytrends.interest_over_time()
trendsTime = pytrends.get_historical_interest(kw_list, year_start=2018, month_start=1, day_start=1, hour_start=0, year_end=2018, month_end=2, day_end=1, hour_end=0, cat=0, geo='', gprop='', sleep=0)
trendsTime.plot(y=["how to breakup"])

#trends.sort_values('date', ascending=True)
#trends.keys()
resample = trends.resample('M').sum()
resample.plot(y=["how to breakup"])


reshapedByMonth = trends.groupby([trends.index.month], as_index=True).sum()
reshapedByMonth.plot()

reshapedByArbitrary = trendsTime.groupby([trendsTime.index.hour], as_index=True).sum()
reshapedByArbitrary.plot()

reshapedByArbitrary = trendsTime.groupby([trendsTime.index.dayofweek], as_index=True).sum()
reshapedByArbitrary.plot()


trends.head()

trends.loc["2018-01-22 15:00:00"]
trends.iloc[0]



trends.iloc[0]
trends.plot(y =['how to breakup'])



trends.groupby([pd.Grouper(freq='1H'), 'how to breakup'])
trends.head()
trends.resample('M').sum()

#interest_over_time_df.loc['2017-10-26']
interest_over_time_df["how to breakup"]

############################################################################
trends.reset_index(level=0, inplace=True)
trends.head()
trends["date"] = pd.to_datetime(trends["date"])
trends.groupby([trends.date.dt.year, trends.date.dt.month]).agg('count')
trends.plot(y =['how to breakup'])
