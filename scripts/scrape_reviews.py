from google_play_scraper import reviews, Sort
import pandas as pd
import os

# App IDs for Ethiopian banks (replace with actual IDs)
app_ids = {
    "Commercial Bank of Ethiopia": "com.combanketh.mobilebanking",
    "Bank of Abyssinia": "com.boa.boaMobileBanking",
    "Dashen Bank": "com.dashen.dashensuperapp"
}

all_reviews = []

for bank, app_id in app_ids.items():
    result, continuation_token = reviews(
        app_id,
        lang='en',
        country='ET',
        sort=Sort.MOST_RELEVANT,
        count=400
    )

    for r in result:
        all_reviews.append({
            "bank": bank,
            "review": r["content"],
            "rating": r["score"],
            "date": r["at"].date()
        })

df = pd.DataFrame(all_reviews)
os.makedirs("data/raw", exist_ok=True)
df.to_csv("data/raw/play_store_reviews.csv", index=False)
print("✅ Scraped reviews saved to data/raw/play_store_reviews.csv")