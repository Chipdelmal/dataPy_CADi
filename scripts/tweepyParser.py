
import tweepy

###############################################################################
# IMPORTANT!
###############################################################################
# Create a file called "twitterCredentials.py" and fill it out with the
#   following information:
#
# access_token =
# access_token_secret =
# consumer_key =
# consumer_secret =
###############################################################################

# Authorizing the package in twitters API
from twitterCredentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

print(user)
print(user.location)


# Using a cursor to get tags from twitter
cursor = tweepy.Cursor(
    api.search,
    q="#unitedAIRLINES",
    count=10,
    lang="en",
    since="2018-25-04"
)
for tweet in cursor.items():
    print (tweet.created_at, tweet.text)
