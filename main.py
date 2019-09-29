from Temper import twitter
from Temper import NLP
from Temper import OWM

print('***----- TEMPER -----***')
print ("""Welcome to the Temper app! This app retrieves tweets within a given radius of a location and performs sentiment analysis on them.
It also retrieves the weather for a given US city and predicts an overall sentiment category (i.e. "postitive", "negative", "neutral", or "mixed") based on that.""")

print("First, let's get some tweets!")
tweets = twitter.get_tweets()

if ( tweets is not None ):
    print("OK! Got a result from the Twitter API.")
    print("Now feeding each tweet into the Google NLP API...")
    total_score = float(0)
    total_magnitude = float(0)
    display_tweets = []

    for tweet in tweets:
        score, magnitude = nlp.get_sentiment(str(tweet.text))
        if ( tweets.num_tweets <= 5 ):
            display_tweets.append( (tweets.num_tweets, tweet.text, tweet.user.screen_name, score, magnitude) )
        total_score += float(score)
        total_magnitude += float(magnitude)

    print('\n----- OVERALL SENTIMENT ANALYSIS -----')
    print("Overall average sentiment score: ", (total_score/tweets.limit) )
    print("Overall average magnitude score: ", (total_magnitude/tweets.limit) )
    print("Overall sentiment label prediction: ", nlp.get_sentiment_label( float(total_score/tweets.limit), float(total_magnitude/tweets.limit) ) )

    print('\nHere\'s a preview of up to 5 tweets....')
    for t in display_tweets:
        print('----- Tweet #', t[0], ' -----')
        print('Made by: @', t[2])
        print(t[1], '\n')
        print('Score: ', t[3], ', Magnitude: ', t[4])
        print( 'Sentiment label: ', nlp.get_sentiment_label(float(t[3]), float(t[4])) )

    print("\nNow let's check the weather. In order for the data to be meaningful, you should really input the same location as before.")
    try:
        w = owm.get_weather()
        print("Today's weather... ")
        print("Wind speed: ", w.wind_speed)
        print("Humidity: ", w.humidity)
        print("High (F): ", w.temp_max)
        print("Low (F): ", w.temp_min)
        print("Current temp (F): ", w.temp_current)
        print("Status (F): ", w.status)

        print("\nBased on the weather forecast, we predict that the overall sentiment is: ", owm.get_sentiment_label_weather(w))
        
        print("\nHow did we do? :)")
        print("Thanks for using the Temper app!")
    except:
        print("Looks like there was some error retrieving the weather information. Please try running the app again.")

else:
    print("Uh oh, looks like we ran into some trouble getting tweets. Please try running the app again.")
