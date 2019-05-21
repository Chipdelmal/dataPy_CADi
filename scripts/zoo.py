# https://data36.com/pandas-tutorial-2-aggregation-and-grouping/
# https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0
# https://data36.com/pandas-tutorial-1-basics-reading-data-files-dataframes-data-selection/


%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

zoo = pd.read_csv("../data/extracted/zoo.csv")

zoo[["animal"]].count()
zoo.animal.count()
animalsList = list(zoo.animal)
animalsTypes = set(animalsList)

waterNeeded = zoo.water_need
waterNeeded.sum()
waterNeeded.min()
waterNeeded.max()
waterNeeded.mean()
waterNeeded.median()
plt.hist(waterNeeded, color = 'blue', edgecolor = 'black',bins = int(180/5))

waterGroupedMean = zoo.groupby("animal").mean()[["water_need"]]
zoo.groupby("animal").mean().water_need

waterGroupedSum = zoo.groupby("animal").mean().water_need
waterGrouped.plot.bar()





article_read = pd.read_csv(
    "../data/extracted/articles.csv",
    delimiter=';',
    names = ['my_datetime', 'event', 'country', 'user_id', 'source', 'topic']
)
article_read[['country', 'user_id']]
article_read[article_read.source == 'SEO']


article_read.groupby('source').count()
article_read[article_read.country == 'country_2'].groupby(['source', 'topic']).count()
