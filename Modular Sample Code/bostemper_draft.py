# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:01:37 2019

@author: jlt15
"""

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "1171248897769058305-0FHc7shhhwl73uy9HM5PFECIWcX10f"
access_token_secret = "Iashw9JPYZFzKePRLm2Q675nWHoz1cxPlK4uGF9QJfbIM"
consumer_key = "gYD2C9HEOxmRrW29zwmOo5EaG"
consumer_secret = "VjIdPbYffVcE5qWykEbUJpnc6zR6w2U4QVwqpFxbqzpkCJc0hK"

class TwitterStreamer():
    def __init__(self):
        pass
    
    def stream_tweets(self, tweets_filename, hashtag_list):
        l = StdOutListener(tweets_filename)
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, l)
        stream.filter(track=hashtag_list)
        
#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def __init__(self,tweets_filename):
        self.tweets_filename = tweets_filename
    
    def on_data(self, data):
        try:   
            print(data)
            with open(self.tweets_filename,'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on data:%s" % str(e))
        return True

    def on_error(self, status):
        print(status) 


if __name__ == '__main__':
    hashtag_list=["Jack Ma"]
    tweets_filename="C:/Users/jlt15/Desktop/tweets.text"
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(tweets_filename, hashtag_list)
    
