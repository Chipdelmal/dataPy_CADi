#   https://spacy.io/usage/linguistic-features#dependency-parse
#   https://towardsdatascience.com/extracting-twitter-data-pre-processing-and-sentiment-analysis-using-python-3-0-7192bd8b47cf
#   https://codereview.stackexchange.com/questions/163446/cleaning-and-extracting-meaningful-text-from-tweets
#   https://github.com/s/preprocessor


#import nltk
#nltk.download("stopwords")


import datetime
import pandas as pd
import preprocessor as p
import re
from nltk.corpus import stopwords
import csv

csv_reader = csv.reader, delimiter = ',')
    with open("../data/extracted/tweepy/crispr.csv", 'r', encoding = "utf-8") as csvFile:
    reader=csv.reader(csvFile)
    for row in reader:
        print(row[1].encode().decode("utf-8", "replace"))

twitterFeed=pd.read_csv(
    "../data/extracted/tweepy/crispr.csv",
    header = None,
    names = ["datetime", "tweet"],
    encoding = "utf-8"
)
    #twitterFeed["datetime"] = pd.to_datetime(twitterFeed["datetime"])
    #twitterFeed["tweet"] = twitterFeed["tweet"].astype(str)
    twitterFeed.dtypes
    twt=twitterFeed["tweet"].iloc[0]


    ################
    uniqueTweets=twitterFeed["tweet"].unique()

    ##########
    twt=uniqueTweets[1]
    doc=nlp(twt)
    print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])

    ##########
    p.set_options()
    twt=twitterFeed["tweet"].iloc[10]
    print(twt)
    p.clean(twt)
    p.parse(twt).urls
