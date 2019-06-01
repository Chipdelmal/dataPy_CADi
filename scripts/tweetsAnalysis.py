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
###############################################################################


###############################################################################
# Import libraries
# import nltk
# nltk.download("stopwords")
import pandas as pd
import preprocessor as p
import re
from nltk.corpus import stopwords
import csv
import spacy
nlp = spacy.load("en_core_web_sm")

###############################################################################
# Load data
twitterFeed = pd.read_csv(
    "../data/extracted/tweepy/crisprBackup.csv",
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
# Get the noun-phrases
twt = p.clean(uniqueTweets[1])
doc = nlp(twt)
nouns = [chunk.text for chunk in doc.noun_chunks]
verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
print(
    "Tweet: " + twt + "\n"
    "Noun phrases: " + str(nouns) + "\n"
    "Verbs: " + str(verbs)
)

###############################################################################
# Parse URLs
p.set_options()
twt = twitterFeed["tweet"].iloc[10]
print(twt)
p.clean(twt)
p.parse(twt).urls




p.clean(twt)
