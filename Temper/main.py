# Given a sentiment score & magnitude,
# uses simple conditionals to determine categorical label
# Returns "positive", "negative", "neutral", or "mixed"
def get_sentiment_label(score, magnitude):
    if (score > 0.25):
        label = "positive"
    elif (score < -0.25):
        label = "negative"
    else:
        label = "neutral"

    if (magnitude < 3.0):
        label = "neutral"

    if ((label == "neutral") and (magnitude >= 3.0)):
        label = "mixed"

    return label

# Uses simple conditionals to predict overall sentiment label
# given a weather object
# def get_sentiment_label_weather(weather):