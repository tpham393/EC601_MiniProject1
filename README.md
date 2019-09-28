# Temper

## Background
As part of the first Mini Project assigned to our EC601 class, our team needs to build a product that sources twitter posts, performs sentiment analysis on these posts, and then conveys that information to the user. There is room for creativity in determining what posts to consider, how to aggregate the sentiment analysis data, and how the information is shared with the product user.

## Introduction
Temper is a twitter sentiment analysis program that specifically searches for the most recent tweets made in a given US city and provides sentiment analysis of those tweets and a prediction of the overall sentiment categorical label based on the current day's local weather forecast. The sentiment analysis is achieved by averaging individual sentiment score and magnitude results from the Google Natural Language API across all tweets, and then assessing whether the average sentiment is "positive," "negative," "neutral," or "mixed" based on the calculated averages. 

The prediction of the categorical label is rudimentary & is as follows:
- "Positive" is predicted if the current temperature >= 75 and the weather status is clouds/clear sky
- "Negative" is predicted if the current temperature <= 50 and the weather status is rain/snow/thunderstorm
- "Mixed" is predicted if the temperature >= 75 and the weather status is rain/snow/thunderstorm OR if the temperature <= 50 and the weather status is clouds/clear sky
- "Neutral" is predicted otherwise

The rudimentary prediction is based on our team's personal experience of the local weather. We decided to use this approach given the limited timeframe to complete this project. A future consideration may be to build in a machine learning algorithm that more accurately predicts the sentiment analysis result based on historical data.

### Inputs to the System:
- Geocode Location: this is entered as a latitude, longitude coordinate-pair with a specified radius in km
- Number of tweets
- US City (for retrieving the weather)

### Outputs of the System:
- Average sentiment score
- Average sentiment magnitude
- Overall categorical label of sentiment
- Current day's weather forecast for Boston (wind speed, humidity, high, low, current temperature, status description)

## How to Use the Program
- Download necessary Python libraries:
  - [tweepy](https://github.com/tweepy/tweepy)
  - [pyowm](https://github.com/csparpa/pyowm)
- Will need API keys for Twitter API and Google NLP API
  - In terminal, set GOOGLE_API_CREDENTIALS by using the following command:
  ```
  $env:GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
  ```
  where [PATH] refers to the location of the .JSON file of your Google NLP API key
- Run main.py located [here](https://github.com/tpham393/EC601_MiniProject1/blob/master/main.py).
- Input OWM API key (can email separately to TA/TF team if requested)

## Product Mission
(subject to change as product develops; current as of 9/28/19)

For your everyday user (any person)
Who is interested in knowing the sentiment analysis of the most recent tweet(s) in a given US city
The product name is “Temper”; it is a Python program
That analyzes the sentiment analysis of the most recent tweet(s) made in a given US city
And allows comparison with the current day’s local weather by displaying weather information with the sentiment analysis result

## User Stories
(subject to change as product develops; current as of 9/28/19)

- I, the user, should be able to get a sentiment analysis (i.e. average of score & magnitude and categorical label of whether it is positive, negative, neutral, or mixed) of the most recent tweets made in US city as of the current time
-	I, the user, should be able to get an overall sentiment analysis (average of score & magnitude and clearly positive, negative, neutral, or mixed) of today’s tweets made in a given US city, which will be an average of the score & magnitude returned by Google’s NLP API
-	I, the user, should be able to specify a number (< maximum allowable as Standard User of Twitter API) of most recent tweets to be analyzed
-	I, the user, should be able to specify a US city (latitude, longitude) and radius value (in miles) for the tweets to be analyzed
-	I, the user, should be able to see today’s weather forecast (high, low, current temp, main description) with the resulting sentiment analysis score
-	I, the user, should be able to preview the most recent tweet(s) being analyzed (up to a certain number)

## Architecture
A diagram of the overall architecture of the program can be found [here](https://github.com/tpham393/EC601_MiniProject1/blob/master/architecture1.png).

Sample code for API callouts can be found in [this folder](https://github.com/tpham393/EC601_MiniProject1/tree/master/Modular%20Sample%20Code).

### Module - Twitter API
We decided to use the Python library [tweepy](https://github.com/tweepy/tweepy) because it seemed more convenient. For example, the professor provided a sample code. There were a lot of additional examples online we could reference to help us figure out how to use the library. It had strong documentation and appeared to be widely used. The library is actively maintained; the latest commit took place within the past month. 
This module asks the user for some inputs (API credentials, geocode location of a US city, number of tweets) and returns an iterable object of the tweets received.

### Module - Google NLP API
The Google NLP API was a project requirement. It has supporting Python libraries, so that is what we used to interface with the API. The libraries include methods to access the individual pieces of information in the resulting JSON, e.g. single out the sentiment score.
This module packages the API callout into a function that accepts the text of the tweet as a parameter and outputs the sentiment score and magnitude. This module also includes a method that uses a series of conditionals to determine a categorical label for the provided sentiment score and magnitude. The if-statements we used were based on our understanding of the Google NLP API documentation; we experimented with the numbers and chose what seemed to make sense by comparing the output label with our personal interpretation of the tweet's sentiment.

### Module - OpenWeatherMap API
OpenWeatherMap API has a free tier of service that accomplishes what we need for this project. In addition, it appeared to be the most recommended on the web for use with Python. There is also a nice wrapper [pyowm](https://github.com/csparpa/pyowm) with straightforward documentation available for use with the OpenWeatherMap API.
This module retrieves the current weather forecast for the provided city. We restricted the country code to US to limit errors/exceptions. It returns the values for the wind speed, humidity, high temperature, low temperature, current temperature, and main status description as a weather object. We created a class structure to simplify how the data would be returned (object vs large tuple). This module also includes a method that uses a series of conditionals to make a rudimentary prediction of the categorical label of the overall sentiment analysis.

### Module - Main
This module runs the entire program/app. It provides a console interface with the app for our users. By organizing the overall structure in this way, our team is practicing the concepts of abstraction & encapsulation. 

## Testing
Screenshots of results can be viewed [here](https://github.com/tpham393/EC601_MiniProject1/tree/master/Test%20Case%20Screenshots).
1. User enters inappropriate Twitter API credentials
2. User enters a geocode location and tweets are returned
3. User enters a geocode location and no tweets are returned
4. User enters inappropriate OWM API credentials
5. User enters name of feasible US city
6. User enters name of infeasible US city

## Lessons Learned
### What you liked doing?
- learning how to use Twitter and Google APIs
- researching additional opensource software/tools to help us develop our product
- implementing process of developing software/product from start to finish
- how organized our timeline/sprints were
- good communication between teammates

### What you could have done better?
- planned more realistically for the allotted timeframe and team's combined skillset (i.e. had too many ambitious goals that were not realized)
- allocated more time to realize some other goals, e.g. develop a user interface, integrate a database into the architecture
- incorporate some kind of filter for "spam" tweets/"scrubbing" the tweets of mentions, links, emojis, etc.
- build something to check that looks up the coordinates of the city the user entered and automatically inputs that information into the OWM module

### What you will avoid in the future?
- researching too many options (i.e. looked at every Python library for Twitter API); should just research a smaller group and decide from there

## Backlog
+ allow input for # of individual results to be displayed 
+ more granular exception handling
+ filter tweets for "spam"
+ incorporate API (Google Maps?) to get latitude, longitude coordinates of US cities for Twitter module & validate that cities entered into the OWM module are in fact in the US
+ database integration to store historical data (weather, tweets, and sentiment score & magnitude)
+ incorporate ML to predict the overall sentiment category label based on training of historical data
+ user interface
+ display data analysis of historical data, i.e. via graph, overlay weather and sentiment trends
