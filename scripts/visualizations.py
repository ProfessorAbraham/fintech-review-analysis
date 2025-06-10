import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("/content/fintech-review-analysis/data/cleaned/themed_reviews.csv")

plt.figure(figsize=(8, 6))
sns.countplot(x="sentiment", hue="bank", data=df)
plt.title("Sentiment Distribution by Bank")
plt.tight_layout()
plt.savefig("/content/fintech-review-analysis/outputs/figures/sentiment_distribution.png")
print("✅ Plot saved to outputs/figures/")
