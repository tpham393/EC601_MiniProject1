# Temper
(ReadMe is a work in progress! 9/23/19)

## Background
As part of the first Mini Project assigned to our EC601 class, our team needs to build a product that sources twitter posts, performs sentiment analysis on these posts, and then conveys that information to the user. There is room for creativity in determining what posts to consider, how to aggregate the sentiment analysis data, and how the information is shared with the product user.

## Introduction
Temper is a twitter sentiment analysis program that specifically searches for the most recent ### tweets made in Boston and provides sentiment analysis of those tweets and a prediction of the overall sentiment categorical label based on the current day's local weather forecast. The sentiment analysis is achieved by averaging individual sentiment score and magnitude results from the Google Natural Language API across all tweets, and then assessing whether the average sentiment is "positive," "negative," "neutral," or "mixed" based on the calculated averages. 

The prediction of the categorical label is rudimentary & is as follows:
- "Positive" is predicted if high is _____ & status is _____
- "Neutral" is predicted if ___________
- "Mixed" is predicted ________
- "Negative" is predicted if __________
The rudimentary prediction is based on our team's personal experience of the local weather. We decided to use this approach given the limited timeframe to complete this project. A future consideration may be to build in a machine learning algorithm that more accurately predicts the sentiment analysis result based on historical data.

### Inputs to the System:
- Location: Boston (this is entered as a latitude, longitude coordinate-pair = ______ with a specified radius = ### )
- Number of tweets: ###

### Outputs of the System:
- Average sentiment score
- Average sentiment magnitude
- Overall categorical label of sentiment
- Current day's weather forecast for Boston (high, low, status description, current temperature)

## How to Use the Program
- Download necessary Python libraries:
  - Tweepy
  - pyowm
- Run main.py located [here](https://github.com/tpham393/EC601_MiniProject1).

## Product Mission
(subject to change as product develops; current as of 9/16/19)

For Bostonians
Who are interested in knowing the sentiment analysis of the most recent local tweet(s)
The product name is “Temper”; it is a Python program
That analyzes the sentiment analysis of the most recent tweet(s) made in Boston
And allows comparison with the current day’s local weather by displaying weather information side-by-side with the sentiment analysis result
[ Unlike other twitter sentiment analysis programs
Our product [targets this very specific application] ]

## User Stories
(subject to change as product develops; current as of 9/16/19)

- I, the user, should be able to get a sentiment analysis (i.e. average of score & magnitude and whether it is clearly positive, negative, neutral, or mixed) of the most recent tweet made in Boston as of the current time
  - “made in Boston” == latitude, longitude coordinates & specified radius (TBD)
-	I, the user, should be able to get an overall sentiment analysis (average of score & magnitude and clearly positive, negative, neutral, or mixed) of today’s tweets made in Boston, which will be an average of the score & magnitude returned by Google’s NLP API
-	I, the user, should be able to specify a date range for the tweets to be analyzed
-	I, the user, should be able to specify a number (< maximum allowable as Standard User of Twitter API) of most recent tweets to be analyzed
-	I, the user, should be able to specify a city (latitude, longitude) and radius value (in miles) for the tweets to be analyzed
-	I, the user, should be able to see today’s weather forecast (high, low, main description, current temp?) laid side-by-side with the sentiment analysis score
-	I, the user, should be able to see a graph/plot (by day) of the sentiment analysis of the tweets specified (if there is more than 1 tweet being considered)
-	I, the user, should be able to see a graph/plot (by day) of the weather forecast’s high & lows overlaid on top of the graph/plot of the sentiment analysis
-	I, the user, should be able to view the most recent tweet(s) being analyzed (up to a certain number)
-	I, the user, should be able to get an analysis about the possible factors which may affect the recent tweets. (TBD)

## Architecture
A diagram of the overall architecture of the program can be found [here](https://github.com/tpham393/EC601_MiniProject1/blob/master/architecture.png)
Sample code for API callouts can be found in [this folder]

### Module - Twitter API
We decided to use the Python library _______ because ________. This module does ________________

### Module - Google NLP API
The Google NLP API was a project requirement. It has supporting Python libraries, so that is what we used to interface with the API. The module packages the API callout into a function that accepts the text of the tweet as a parameter and outputs the JSON response of the API. It also stores the JSON response in the proper node of the Firebase Database.

### Module - OpenWeatherMap API
OpenWeatherMap API has a free tier of service that accomplishes what we need. In addition, it appeared to be the most recommended on the web for use of Python. There is also a nice wrapper [pyowm](https://github.com/csparpa/pyowm) with straightforward documentation available for use with the OpenWeatherMap API.
This module retrieves the current weather forecast for the provided city and/or (latitude, longitude) coordinate-pair with ___(some radius?)____. It returns/prints the values for the high temperature, low temperature, current temperature, and main status description. 

### Module - Main
.......blah........
Based on the output of the OpenWeatherMap module, the main program uses a set of if-statements/switch statement to make a rudimentary "prediction" of the categorical label of the overall sentiment analysis.

