import twitter
import json
import yweather

from twitterCredentials import *

auth = twitter.oauth.OAuth(
    access_token, access_token_secret,
    consumer_key , consumer_secret
)

twitter_api = twitter.Twitter(auth=auth)
client = yweather.Client()
id = client.fetch_woeid('Mexico')

# https://developer.twitter.com/en/docs/trends/trends-for-location/api-reference/get-trends-place.html
# https://en.wikipedia.org/wiki/WOEID
WORLD_WOE_ID = 1
US_WOE_ID = 23424977
MX_WOE_ID = int(id)

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)
mx_trends = twitter_api.trends.place(_id=MX_WOE_ID)

print(world_trends)
print(us_trends)
print(mx_trends)

print(json.dumps(world_trends, indent=1))
print(json.dumps(us_trends, indent=1))
print(json.dumps(mx_trends, indent=1))


[trend['name'] for trend in mx_trends[0]["trends"]]
