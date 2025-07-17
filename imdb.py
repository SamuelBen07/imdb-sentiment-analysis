from google.colab import files
uploaded = files.upload()
import pandas as pd


df = pd.read_csv("imdb_top_1000.csv")

df.head()

df.info()


df.isnull().sum()


df['sentiment'].value_counts()
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub(r'<.*?>', '', str(text))                   
    text = re.sub(r'[^a-zA-Z]', ' ', text)                   
    words = text.lower().split()                             
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

df['cleaned_overview'] = df['Overview'].apply(clean_text)
from textblob import TextBlob

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return 'positive'
    elif polarity == 0:
        return 'neutral'
    else:
        return 'negative'

df['sentiment'] = df['cleaned_overview'].apply(get_sentiment)
df[['Series_Title', 'Overview', 'sentiment']].head(10)
df['sentiment'].value_counts().plot(kind='bar', title='Sentiment Distribution')
TextBlob(text).sentiment
TextBlob("This movie was terrible").sentiment.polarity
if polarity > 0:
    return 'positive'
elif polarity == 0:
    return 'neutral'
else:
    return 'negative'
df['polarity'] = df['cleaned_overview'].apply(lambda x: TextBlob(x).sentiment.polarity)
df['subjectivity'] = df['cleaned_overview'].apply(lambda x: TextBlob(x).sentiment.subjectivity)

df[['Series_Title', 'polarity', 'subjectivity', 'sentiment']].head()
from textblob import TextBlob

df['polarity'] = df['cleaned_overview'].apply(lambda x: TextBlob(x).sentiment.polarity)
df['subjectivity'] = df['cleaned_overview'].apply(lambda x: TextBlob(x).sentiment.subjectivity)
