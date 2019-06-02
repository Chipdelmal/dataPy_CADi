# -*- coding: utf-8 -*-

###############################################################################
# "pytrends" example
###############################################################################
#  Objectives:
#   To test the Google Trends data retreival within Python
#  Source:
#   https://github.com/GeneralMills/pytrends#api
#   https://brohrer.github.io/dataframe_indexing.html
#   https://github.com/GeneralMills/pytrends
#   https://towardsdatascience.com/heartbreak-monday-blues-and-pytrends-f1a398591a79
#   https://data36.com/pandas-tutorial-2-aggregation-and-grouping/
###############################################################################

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Import required libraries
from pytrends.request import TrendReq
from matplotlib import rcParams
%matplotlib inline
rcParams.update({'figure.autolayout': True})

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Defining the trends request
#   https://trends.google.com/trends/explore?q=blockchain&geo=US
kw_list = ["data"]
pytrends = TrendReq(hl='en-US', tz=360)
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Interest Over Time
interest_over_time_df = pytrends.interest_over_time()
# interest_over_time_df.loc['2017-10-26']
print(interest_over_time_df.head())
interest_over_time_df["data"].plot()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Interest by Region
interest_by_region_df = pytrends.interest_by_region()
interest_by_region_df.sort_values(by=["data"], ascending=False, inplace=True)
interest_by_region_df.iloc[:20].plot.bar()
# fig = interest_by_region_df.iloc[:20].plot.bar()
# fig.get_figure().savefig('trends.png',dpi=500)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Related Queries, returns a dictionary of dataframes
related_queries_dict = pytrends.related_queries()
print(related_queries_dict)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Get Google Keyword Suggestions
suggestions_dict = pytrends.suggestions(keyword='pizza')
print(suggestions_dict)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Get Google Hot Trends data
trending_searches_df = pytrends.trending_searches()
print(trending_searches_df.head())

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Get Google Top Charts
top_charts_df = pytrends.top_charts(cid='actors', date=201611)
print(top_charts_df.head())
