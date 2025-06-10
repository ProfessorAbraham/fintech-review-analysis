import pandas as pd
import os

df = pd.read_csv("data/raw/play_store_reviews.csv")

# Remove duplicates
df.drop_duplicates(subset=["review"], inplace=True)

# Handle missing values
df.dropna(subset=["review"], inplace=True)

# Normalize date format
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

# Save cleaned data
os.makedirs("/content/fintech-review-analysis/data/cleaned", exist_ok=True)
df.to_csv("/content/fintech-review-analysis/data/cleaned/cleaned_reviews.csv", index=False)
print("✅ Cleaned reviews saved to data/cleaned/cleaned_reviews.csv")
