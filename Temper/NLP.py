# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def get_sentiment(input_text):
    # Instantiates a client
    client = language.LanguageServiceClient()

    # The text to analyze
    document = types.Document(
        content=input_text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    return sentiment.score, sentiment.magnitude

# Test code for above method
score, magnitude = get_sentiment('I am really happy today!!!')
print('Sentiment score: ', score)
print('Sentiment magnitude: ', magnitude)