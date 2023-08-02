import tweepy
import s3fs
import json
import pandas as pd
from datetime import datetime


def run_twitter_etl():
    
    access_key = ""
    access_secret = ""
    consumer_key = ""
    consumer_secret = ""

    # Provide Twitter authentication here
    auth = tweepy.OAuthHandler(access_key, access_secret)
    auth.set_access_token(consumer_key, consumer_secret)

    # Create an API object
    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name = '@elonmusk',
                            count = 1500, include_rts = False,
                            tweet_mode = 'extended')
    #print(tweets) # Print the tweets in json formats from terminal to see that it's working


    tweet_list = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {"user": tweet.user.screen_name, "text" : text,
                        "favorite_count" : tweet.favorite_count,
                        "created_at" : tweet.created_at}
        
        tweet_list.append(refined_tweet)

        df = pd.DataFrame(tweet_list)
        df.to_csv("Twitter_data.csv")

