# https://stackabuse.com/accessing-the-twitter-api-with-python/
# https://www.pythoncentral.io/introduction-to-tweepy-twitter-for-python/
# https://gist.github.com/vickyqian/f70e9ab3910c7c290d9d715491cde44c
# https://gist.github.com/dev-techmoe/ef676cdd03ac47ac503e856282077bf2
# http://docs.tweepy.org/en/v3.5.0/cursor_tutorial.html
# 429 Too Many Requests

import tweepy



# consumer_key =
# consumer_secret =
# access_token =
# access_token_secret =

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

print(user.location)
user


cursor = tweepy.Cursor(
    api.search,
    q="#unitedAIRLINES",
    count=10,
    lang="en",
    since="2019-25-04"
)
for tweet in cursor.items():
    print (tweet.created_at, tweet.text)

tweet.text
