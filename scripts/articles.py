# -*- coding: utf-8 -*-

###############################################################################
# "Articles" example
###############################################################################
#  Objectives:
#   Learning the basics of aggregation in pandas dataframes
#  Sources:
#   https://data36.com/pandas-tutorial-2-aggregation-and-grouping/
#   https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0
#   https://data36.com/pandas-tutorial-1-basics-reading-data-files-dataframes-data-selection/
###############################################################################

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Import libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
%matplotlib inline

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Loading the dataset
article_read = pd.read_csv(
    "../data/extracted/pandas/articles.csv",
    delimiter=';',
    names=['my_datetime', 'event', 'country', 'user_id', 'source', 'topic']
)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# A little exploration
article_read
article_read[['country', 'user_id']]
article_read[article_read.source == 'SEO']

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Group and aggregate
article_read.groupby('source').count()
readByCountryTwo = article_read[article_read.country == 'country_2']
readByCountryTwo.groupby(['source', 'topic']).count()
