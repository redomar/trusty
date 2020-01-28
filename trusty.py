import tweepy
import time
import os
from dotenv import load_dotenv

load_dotenv()

API_key = os.getenv("API_key")
API_secret_key = os.getenv("API_secret_key")
API_token = os.getenv("API_token")
API_token_secret = os.getenv("API_token_secret")

auth = tweepy.OAuthHandler(API_key, API_secret_key)
auth.set_access_token(API_token, API_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = "Synthwave"
nrTweets = 25

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        if tweet.favorite_count >= 10:
            print(f"Tweet Liked From {tweet.author.screen_name}")
            tweet.favorite()
            time.sleep(90)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
