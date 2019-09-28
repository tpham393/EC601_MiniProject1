# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def get_sentiment(input_text):
    try:
        # Instantiates a client
        client = language.LanguageServiceClient()

        # The text to analyze
        document = types.Document(
            content=input_text,
            type=enums.Document.Type.PLAIN_TEXT)

        # Detects the sentiment of the text
        sentiment = client.analyze_sentiment(document=document).document_sentiment

        return sentiment.score, sentiment.magnitude
        
    except:
        print("Some error occurred trying to process request to Google NLP API.")

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

    if ((label == "neutral") and (magnitude >= 2.5)):
        label = "mixed"

    return label

# Test code for above methods
if __name__ == '__main__':
    print('----- TEST FOR NLP MODULE ----- \n')

    print('*** Testing get_sentiment method ***')
    score, magnitude = get_sentiment('I am really happy today!!!')
    print('Sentiment score: ', score)
    print('Sentiment magnitude: ', magnitude)

    print('\n')
    print('*** Testing get_sentiment_label method ***')
    # Test for "positive" label
    print('Score: 0.75, Magnitude: 5.0')
    print( 'Sentiment label: ', get_sentiment_label(0.75, 5.0) )

    # Test for "negative" label
    print('Score: -0.3, Magnitude: 5.0')
    print( 'Sentiment label: ', get_sentiment_label(-0.3, 5.0) )

    # Test for "neutral" label
    print('Score: 0.0, Magnitude: 0.0')
    print( 'Sentiment label: ', get_sentiment_label(0, 0) )

    # Test for "mixed" label
    print('Score: 0.2, Magnitude: 3.0')
    print( 'Sentiment label: ', get_sentiment_label(0.2, 3.0) )

    print('\n')
    print('----- END TEST FOR NLP MODULE -----')