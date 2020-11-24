import tweepy
import time
from config import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

tweets = tweepy.Cursor(api.search, q=('#100DaysOfCode OR #Python -filter:retweets'), lang='en').items(5)

def searchRetweet():
    for tweet in tweets:
        print("Searching Tweets...")
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(10)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(10)

searchRetweet()