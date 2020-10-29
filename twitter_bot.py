import tweepy
from textblob import TextBlob
import numpy as np

consumer_key=''
consumer_secret=''

access_token=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

tweets = api.search('PS5')
score = []

for tweet in tweets:
    frase = TextBlob(tweet.text)
    score.append(frase.sentiment.polarity)

    if frase.detect_language() != 'en':
        traducao = TextBlob(str(frase.translate(to='en')))
        print('Tweet: {0} \nSentimento: {1}\n'.format(tweet.text, traducao.sentiment))
    else:
        print('Tweet: {0} \nSentimento: {1}\n'.format(tweet.text, frase.sentiment))

print('Média de sentimento: {0}'.format(np.mean(score)))