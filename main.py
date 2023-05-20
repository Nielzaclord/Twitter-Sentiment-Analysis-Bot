import tweepy
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
from config import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Authentification avec l'API de Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Recherche de tweets
public_tweets = api.search('Bitcoin', count=100, lang='en')

# Analyse de sentiment
data = {'Tweet': [], 'Polarity': [], 'Subjectivity': []}
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    data['Tweet'].append(tweet.text)
    data['Polarity'].append(analysis.sentiment.polarity)
    data['Subjectivity'].append(analysis.sentiment.subjectivity)

df = pd.DataFrame(data)

# Visualisation
plt.figure(figsize=(10, 10))
plt.scatter(df['Polarity'], df['Subjectivity'], color='Blue')
plt.title('Sentiment Analysis')
plt.xlabel('Polarity')
plt.ylabel('Subjectivity')
plt.show()
