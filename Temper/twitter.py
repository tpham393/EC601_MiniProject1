# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 19:57:45 2019

@author: jlt15
@editor: thuyp
"""

def get_tweets():
    try:
        import json
    except ImportError:
        import simplejson as json
    import tweepy
    #Variables that contains the user credentials to access Twitter API 
    access_token = input("Please input your access_token: ")
    access_token_secret = input("Please input your access_token_secert: ")
    consumer_key = input("Please input your consumer_key: ")
    consumer_secret = input("Please input your consumer_secret: ")

    from tweepy import OAuthHandler
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    try:
        api=tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
        #print(api.get_status())

        if ( api is not None ):
            print("Now retrieving tweets by geocode location (latitude, longitude) and surrounding radius.")
            print("Please input information for a US city of your choice.")
            print("FYI: The latitude, longitude for Boston, MA, USA is 42.3611, -71.0571.")
            latitude = input("Please input the latitude: ")
            longitude = input("Please input the longitude: ")
            radius=input("Please input the radius you want (unit:km): ")
            num_of_tweets = int(input("Please input the # of the tweets you want to retreive: "))

            try:
                back_tweets = tweepy.Cursor(api.search, 
                    geocode=latitude+','+ longitude+','+ radius+'km', 
                    lang='en', 
                    count=num_of_tweets, 
                    result_type='recent', 
                    exclude_replies=True).items(num_of_tweets)

                if ( back_tweets is not None ):
                    return back_tweets
                else:
                    print("There were no tweets to retrieve at that location with the given radius.")

            except:
                print("You did not correctly input all of the necessary criteria.")
        else:
            print("Unable to authenticate Twitter API access with provided credentials.")

    except:
        print("Unable to authenticate Twitter API access with provided credentials.")

# Test code for above method
if __name__ == '__main__':
    print('----- TEST FOR TWITTER MODULE -----')
    tweets = get_tweets()

    for tweet in tweets:
        print('----- Tweet #', tweets.num_tweets, ' -----')
        print('Made by: @', tweet.user.screen_name)
        print(tweet.text, '\n')

    print('----- END TEST FOR TWITTER MODULE -----')
