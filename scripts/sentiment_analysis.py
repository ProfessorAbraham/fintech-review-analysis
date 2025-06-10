from textblob import TextBlob
import pandas as pd

df = pd.read_csv("/content/fintech-review-analysis/data/cleaned/cleaned_reviews.csv")

def get_sentiment(review):
    analysis = TextBlob(review)
    return "positive" if analysis.sentiment.polarity > 0 else "negative"

df["sentiment"] = df["review"].apply(get_sentiment)
df.to_csv("/content/fintech-review-analysis/data/cleaned/sentiment_reviews.csv", index=False)
print("✅ Sentiment analysis complete and saved.")
