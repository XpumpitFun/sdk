import tweepy
from config import TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET

def create_twitter_client():
    auth = tweepy.OAuth1UserHandler(
        TWITTER_API_KEY, TWITTER_API_SECRET,
        TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET
    )
    api = tweepy.API(auth)
    return api

def reply_to_tweet(api, tweet_id, message):
    api.update_status(status=message, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)
