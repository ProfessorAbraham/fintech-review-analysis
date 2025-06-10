from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

df = pd.read_csv("/content/fintech-review-analysis/data/cleaned/sentiment_reviews.csv")

vectorizer = TfidfVectorizer(stop_words='english', max_features=100)
tfidf_matrix = vectorizer.fit_transform(df['review'])

feature_names = vectorizer.get_feature_names_out()
dense = tfidf_matrix.mean(axis=0).A1
top_keywords = [feature_names[i] for i in dense.argsort()[-10:][::-1]]

themes = {
    "User Interface": ["ui", "interface", "easy", "good"],
    "Crashes & Bugs": ["crash", "error", "freeze", "bug"],
    "Speed": ["slow", "fast", "loading", "quick"]
}

print("Top Keywords:", top_keywords)
print("Themes Identified:", themes)

# Optional: Add theme column
def assign_theme(review):
    review = review.lower()
    if any(word in review for word in themes["User Interface"]):
        return "User Interface"
    elif any(word in review for word in themes["Crashes & Bugs"]):
        return "Crashes & Bugs"
    elif any(word in review for word in themes["Speed"]):
        return "Speed"
    else:
        return "Other"

df["theme"] = df["review"].apply(assign_theme)
df.to_csv("/content/fintech-review-analysis/data/cleaned/themed_reviews.csv", index=False)
print("✅ Thematic analysis complete and saved.")
