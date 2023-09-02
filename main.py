from parameters import *
import tweepy

auth = tweepy.OAuth1UserHandler(
    consumer_key=API_KEY, consumer_secret=API_KEY_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET
)

api = tweepy.API(auth)

client = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_KEY_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

client.get_tweet()