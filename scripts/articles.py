# https://data36.com/pandas-tutorial-2-aggregation-and-grouping/
# https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0
# https://data36.com/pandas-tutorial-1-basics-reading-data-files-dataframes-data-selection/


%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

article_read = pd.read_csv(
    "../data/extracted/pandas/articles.csv",
    delimiter=';',
    names = ['my_datetime', 'event', 'country', 'user_id', 'source', 'topic']
)
article_read[['country', 'user_id']]
article_read[article_read.source == 'SEO']


article_read.groupby('source').count()
article_read[article_read.country == 'country_2'].groupby(['source', 'topic']).count()
