# imdb-sentiment-analysis
Sentiment analysis on IMDB movie reviews using NLP and Machine Learning.
# 🎬 IMDB Sentiment Analysis

This project performs sentiment analysis on IMDB movie reviews using Natural Language Processing (NLP) and Machine Learning. It classifies reviews as **positive** or **negative** based on the textual content.

---

## 📌 Project Overview

- **Goal**: Predict sentiment (Positive/Negative) from IMDB reviews.
- **Tech Stack**: Python, Scikit-learn, Pandas, Flask (optional), HTML/CSS.
- **ML Model**: Logistic Regression (or any model you've used).

---

## 🧠 Key Features

- Text preprocessing: removing stopwords, stemming/lemmatization.
- Vectorization using CountVectorizer / TF-IDF.
- Model training and evaluation.
- Web UI using Flask (if applicable).
- Displays real-time prediction from user input.

---

🧩 Process:
Loaded and explored the dataset using pandas and df.info().

Discovered the dataset doesn’t contain user reviews — instead, I creatively used the movie descriptions (Overview) for sentiment.

Cleaned the text: removed HTML tags, stopwords, symbols, and converted everything to lowercase.

Applied TextBlob’s polarity scoring to extract sentiment based on description tone.

Added polarity and subjectivity columns for deeper analysis.

Created visualizations showing sentiment distribution, polarity vs. subjectivity, and comparison with IMDB ratings.



