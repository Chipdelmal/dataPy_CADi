# -*- coding: utf-8 -*-

###############################################################################
# "Twitter Tools" example
###############################################################################
#  Objectives:
#   Using tweepy to parse twitter tags
#  Source:
#   https://mike.verdone.ca/twitter/
#   https://developer.twitter.com/en/docs/trends/trends-for-location/api-reference/get-trends-place.html
#   https://en.wikipedia.org/wiki/WOEID
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
from twitter import *
import twitter
import json
import yweather
import nltk
from collections import Counter

# Authorizing the package in twitters API
from twitterCredentials import *

auth = twitter.oauth.OAuth(
    access_token, access_token_secret,
    consumer_key, consumer_secret
)

# Initializing an API session
twitter_api = twitter.Twitter(auth=auth)
print(twitter_api)

###############################################################################
# Getting the trends information from locations in the world
WORLD_WOE_ID = 1
US_WOE_ID = 23424977

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

print(us_trends)
print(json.dumps(us_trends, indent=1))

# Getting trends information with auto-fetch of WOEID
client = yweather.Client()
id = client.fetch_woeid('Germany')
MX_WOE_ID = int(id)
MX_WOE_ID
mx_trends = twitter_api.trends.place(_id=MX_WOE_ID)
mxTrends = [(trend['name'], trend["tweet_volume"]) for trend in mx_trends[0]["trends"]]
print(mxTrends)




###############################################################################
# More operations with "Python Twitter Tools"
t = Twitter(
    auth=OAuth(
        access_token, access_token_secret,
        consumer_key, consumer_secret
    ),
    retry=True
)
t.statuses.home_timeline()
t.statuses.home_timeline(count=5)


###############################################################################
# Twitting to my timeline
# t.statuses.update(status="10001010101110101011010010100101010010101011111")

pyConTag = t.search.tweets(q=["#CRISPR", "#CAS9"])
pyConTag.keys()
print(pyConTag["statuses"][0])
print(pyConTag["statuses"][0]['user'])


pyConTagExt = t.search.tweets(q=["#CRISPR", "#CAS9"], tweet_mode='extended')
[i["full_text"] for i in pyConTagExt["statuses"]]
