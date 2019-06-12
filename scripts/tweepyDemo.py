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
#   https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object.html
#   https://gist.github.com/dev-techmoe/ef676cdd03ac47ac503e856282077bf2
#   http://best-hashtags.com/hashtag/
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

###############################################################################
# Authorizing the package in twitters API
from twitterCredentials import (
    consumer_key, consumer_secret,
    access_token, access_token_secret
)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
user = api.me()

# print(user)
# print(user.location)

###############################################################################
# Using a cursor to get tags from twitter
maxTweets = 100
tagText = "#pycon"
sinceDate = "2019-01-01"

###############################################################################
# Open/Create a file to append data
csvFile = open(
    '../data/extracted/Tweepy/' + tagText.split("#")[1] + ".csv",
    'w'
)
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(
            api.search, q=tagText, count=maxTweets,
            lang="en", since=sinceDate, tweet_mode='extended'
        ).items():
    # print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.full_text])
print("Finished!")
csvFile.close()

###############################################################################
# Exploring the structure
tweet.full_text
