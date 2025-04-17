import matplotlib.pyplot as plt
import seaborn as sns

# Make plots prettier
sns.set(style='whitegrid')
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='sentiment', palette='pastel')
plt.title('Sentiment Distribution in Movie Overviews')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='polarity', y='subjectivity', hue='sentiment', palette='Set2')
plt.title('Polarity vs Subjectivity')
plt.xlabel('Polarity (-1 to +1)')
plt.ylabel('Subjectivity (0 to 1)')
plt.show()
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='sentiment', y='IMDB_Rating', palette='coolwarm')
plt.title('IMDB Rating vs Sentiment')
plt.xlabel('Sentiment')
plt.ylabel('IMDB Rating')
plt.show()
