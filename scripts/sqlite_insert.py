import sqlite3
import pandas as pd

# Create SQLite database (in-memory or file-based)
connection = sqlite3.connect("/content/fintech-review-analysis/data/reviews.db")
cursor = connection.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS banks (
        bank_id INTEGER PRIMARY KEY,
        bank_name TEXT NOT NULL UNIQUE
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        review_id INTEGER PRIMARY KEY AUTOINCREMENT,
        bank_id INTEGER,
        review_text TEXT,
        rating INTEGER,
        date_posted DATE,
        sentiment TEXT,
        theme TEXT,
        FOREIGN KEY (bank_id) REFERENCES banks(bank_id)
    )
''')

# Load themed reviews
df = pd.read_csv("/content/fintech-review-analysis/data/cleaned/themed_reviews.csv")

# Map bank names to IDs
banks = {name: idx+1 for idx, name in enumerate(df['bank'].unique())}

# Insert banks
cursor.executemany('''
    INSERT OR IGNORE INTO banks (bank_id, bank_name) VALUES (?, ?)
''', [(idx, name) for name, idx in banks.items()])

# Insert reviews
for _, row in df.iterrows():
    cursor.execute('''
        INSERT INTO reviews (bank_id, review_text, rating, date_posted, sentiment, theme)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        banks[row['bank']],
        row['review'],
        row['rating'],
        row['date'],
        row['sentiment'],
        row['theme']
    ))

# Commit and close
connection.commit()
cursor.close()
connection.close()

print("✅ Data inserted into SQLite database at /content/fintech-review-analysis/data/reviews.db")
