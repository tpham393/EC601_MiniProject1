# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 19:57:45 2019

@author: jlt15
"""
try:
    import json
except ImportError:
    import simplejson as json
import tweepy
#Variables that contains the user credentials to access Twitter API 
access_token = input("please input your access_token:")
access_token_secret = input("please input your access_token_secert:")
consumer_key = input("please input your consumer_key:")
consumer_secret = input("please input your consumer_secret:")
from tweepy import OAuthHandler
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api=tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

print("The latitude of Boston, MA, USA is 42.3611, and the longitude is -71.0571. ")
(latitude, longtitude)=input("please input the latitude and longtitude:").split()
radius=input("please input the radius you want(unit:km):")
num_of_tweets = int(input("please input the amount of the tweetes you want to retreive:"))

back_tweets = tweepy.Cursor(api.search, geocode=latitude+','+ longtitude+','+ radius+'km').items(num_of_tweets)
for tweet in back_tweets:
    print(tweet.text+'\n')
    
