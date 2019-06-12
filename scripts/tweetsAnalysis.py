# -*- coding: utf-8 -*-

###############################################################################
# "Tweets Analysis" Script
###############################################################################
#  Objectives:
#   Loading tweets stored in a CSV and doing some processing on them
#  Sources:
#   https://spacy.io/usage/linguistic-features#dependency-parse
#   https://towardsdatascience.com/extracting-twitter-data-pre-processing-and-sentiment-analysis-using-python-3-0-7192bd8b47cf
#   https://codereview.stackexchange.com/questions/163446/cleaning-and-extracting-meaningful-text-from-tweets
#   https://github.com/s/preprocessor
#   https://textblob.readthedocs.io/en/dev/quickstart.html
#   https://www.analyticsvidhya.com/blog/2018/02/natural-language-processing-for-beginners-using-textblob/
###############################################################################
#   Instructions:
#
# pip install spacy
# pip install nltk
# pip install textblob
# pip install preprocessor
# python -m spacy download en_core_web_sm
# python -m textblob.download_corpora

# python import nltk
# nltk.download("stopwords")

###############################################################################
# Import libraries
# import nltk
from textblob import TextBlob
import pandas as pd
import preprocessor as p
import statistics
from nltk.corpus import stopwords
import csv
import numpy as np
import seaborn as sns
nlp = spacy.load("en_core_web_sm")
%matplotlib inline


###############################################################################
# Load data
twitterFeed = pd.read_csv(
    "../data/extracted/tweepy/crispr.csv",
    header=None,
    names=["datetime", "tweet"],
    encoding="utf-8"
)
twitterFeed.dtypes

###############################################################################
# Correct date to datetime type
twitterFeed["datetime"] = pd.to_datetime(twitterFeed["datetime"])
twt = twitterFeed["tweet"].iloc[0]
twitterFeed.dtypes

###############################################################################
# Getting the non-repeated tweets
uniqueTweets = twitterFeed["tweet"].unique()
len(uniqueTweets)
uniqueTweets[0]

###############################################################################
# Deleting RTs
isRT = [txt[0:3]!="RT " for txt in uniqueTweets]
uniqueNonRT = uniqueTweets[isRT]

###############################################################################
# Get the noun-phrases
p.set_options()
twt = p.clean(uniqueNonRT[1])
doc = nlp(twt)
nouns = [chunk.text for chunk in doc.noun_chunks]
verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
print(
    "Tweet: " + twt + "\n"
    "Noun phrases: " + str(nouns) + "\n"
    "Verbs: " + str(verbs)
)

###############################################################################
# Sentiment
#   Polarity is float which lies in the range of [-1,1] where 1 means positive
#       statement and -1 means a negative statement.
#   Subjective sentences generally refer to personal opinion, emotion or
#       judgment whereas objective refers to factual information. Subjectivity
#       is also a float which lies in the range of [0,1].
twt = p.clean(uniqueNonRT[0])
blob = TextBlob(twt)
(polarity, subjectivity) = blob.sentiment
print(
    twt + "\n"
    "P: " + str(polarity) + "\n" +
    "S: " + str(subjectivity)
)

###############################################################################
# Sentiment Plots
polarities = []
for txt in uniqueNonRT:
    twt = p.clean(txt)
    blob = TextBlob(twt)
    (polarity, subjectivity) = blob.sentiment
    polarities.append(polarity)
statistics.mean(polarities)
sns.distplot(polarities)
sns.violinplot(polarities)
