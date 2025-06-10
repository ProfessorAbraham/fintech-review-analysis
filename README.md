## **Customer Experience Analytics for Fintech Apps**  
 A data engineering and NLP project to analyze user reviews of Ethiopian banks' mobile apps using web scraping, sentiment analysis, thematic clustering, visualization, and Oracle database integration.

---

## 🔍 Project Overview

This repository contains the complete pipeline for collecting, analyzing, and storing Google Play Store reviews for three Ethiopian banks:

- **Commercial Bank of Ethiopia (CBE)**
- **Bank of Abyssinia (BOA)**
- **Dashen Bank**

The goal is to extract customer satisfaction drivers and pain points to help improve mobile banking experiences. The output includes:

- Cleaned review datasets
- Sentiment and theme-based insights
- Visualizations
- Structured relational storage (Oracle-ready schema)

This project simulates the role of a Data Analyst at Omega Consultancy advising banks on app improvements.

---

## 🧰 Technologies Used

| Tool/Library | Purpose |
|--------------|---------|
| `google-play-scraper` | Scraping reviews from the Google Play Store |
| `pandas`, `numpy` | Data manipulation and preprocessing |
| `textblob`, `transformers` | Sentiment analysis |
| `scikit-learn`, `spaCy` | Keyword extraction and thematic analysis |
| `matplotlib`, `seaborn` | Visualization |
| `cx_Oracle` / `oracledb` | Oracle database connection |
| `SQLite` | Local development fallback |
| `Git` | Version control |
| `Jupyter Notebooks` | Interactive exploration |

---


---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/fintech-review-analytics.git
cd fintech-review-analytics
```
### 2. Install Dependencies
```bash
Copy
Edit
pip install -r requirements.txt
```
⚠️ For Oracle DB support: Ensure Oracle Instant Client is installed and configured.

#### 🕵️ Task 1: Scrape & Preprocess Reviews
Scrape at least 400 reviews per bank, clean them, and save to CSV.

```bash
Copy
Edit
python scripts/scrape_reviews.py
python scripts/preprocess_reviews.py
```

Output:
```
data/raw/play_store_reviews.csv

data/cleaned/cleaned_reviews.csv
```
#### 😊 Task 2: Sentiment & Thematic Analysis
Use TextBlob for sentiment analysis and TF-IDF for keyword extraction.
```
bash
Copy
Edit
python scripts/sentiment_analysis.py
python scripts/theme_analysis.py
```

Outputs:
```
data/cleaned/sentiment_reviews.csv

data/cleaned/themed_reviews.csv
```
#### 🗃️ Task 3: Store in Oracle DB
Oracle schema and fallback SQLite script included.
```
scripts/oracle_schema.sql — Oracle-compatible schema

scripts/sqlite_insert.py — Insert to SQLite
```
#### 📊 Task 4: Insights & Visualizations
Generate plots and summary insights.
```
bash
Copy
Edit
python scripts/visualizations.py
```

Output:
```
outputs/figures/sentiment_distribution.png
```
### 📝 Final Report
A 7-page report with actionable insights and visualizations.

Location: ``` outputs/reports/report.md```

##### Covers CBE, BOA, and Dashen Bank

 📌 KPIs Metrics
---
KPI	Status
1200+ clean reviews	✅ 

<5% missing data	✅

Git version control	✅

Sentiment scores for all reviews	✅

3+ themes per bank	✅

Oracle schema implemented	✅

7+ visualizations	✅

4+ page professional report	✅

---
### 🧪 Unit Testing & Documentation
Modular code with comments
```
.gitignore and README.md included
```
Extendable for pytest or unittest

📬 Contact
For questions or collaboration:

📧 Email: abrahamdagne64@gmail.com
🔗 GitHub: @professorabraham

📜 License
MIT License — Free to use, modify, and distribute.
