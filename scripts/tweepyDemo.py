# -*- coding: utf-8 -*-

###############################################################################
# "Tweepy" example
###############################################################################
#  Objectives:
#   Using tweepy to parse twitter tags and writting them to a CSV file
#  Sources:
#   https://www.tweepy.org/
#   https://gist.github.com/vickyqian/f70e9ab3910c7c290d9d715491cde44c
#   http://www.compciv.org/homework/assignments/twitter_csv_analysis/
###############################################################################
# IMPORTANT!
#   Create a file called "twitterCredentials.py" and fill it out with the
#       following information:
#
# access_token =
# access_token_secret =
# consumer_key =
# consumer_secret =
###############################################################################

###############################################################################
# Import libraries
import tweepy
import csv
import unicodedata
import io

###############################################################################
# Authorizing the package in twitters API
from twitterCredentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
user = api.me()

# print(user)
# print(user.location)

###############################################################################
# Using a cursor to get tags from twitter
maxTweets = 10
tagText = "#crispr"
sinceDate = "2017-04-03"

###############################################################################
# Open/Create a file to append data
csvFile = open(
    '../data/extracted/Tweepy/' + tagText.split("#")[1] + ".csv",
    'w',
    encoding='UTF-8'
)
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search, q=tagText, count=maxTweets, lang="en", since=sinceDate).items():
    # print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('UTF-8')])
print("Finished!")
