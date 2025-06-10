import cx_Oracle
import pandas as pd

# Replace with your actual Oracle DB credentials and connection string
connection = cx_Oracle.connect('your_username/your_password@localhost/ORCL')
cursor = connection.cursor()

# Create banks table
cursor.execute("""
    BEGIN
        EXECUTE IMMEDIATE 'DROP TABLE reviews';
        EXECUTE IMMEDIATE 'DROP TABLE banks';
    EXCEPTION
        WHEN OTHERS THEN
            IF SQLCODE != -942 THEN
                RAISE;
            END IF;
    END;
""")

cursor.execute("""
    CREATE TABLE banks (
        bank_id NUMBER PRIMARY KEY,
        bank_name VARCHAR2(100) UNIQUE
    )
""")

# Create reviews table
cursor.execute("""
    CREATE TABLE reviews (
        review_id NUMBER PRIMARY KEY,
        bank_id NUMBER,
        review_text CLOB,
        rating NUMBER,
        date_posted DATE,
        sentiment VARCHAR2(10),
        theme VARCHAR2(50),
        CONSTRAINT fk_bank FOREIGN KEY (bank_id) REFERENCES banks(bank_id)
    )
""")

# Load cleaned CSV
df = pd.read_csv("/content/fintech-review-analysis/data/cleaned/themed_reviews.csv")

# Insert banks
banks = {name: idx+1 for idx, name in enumerate(df['bank'].unique())}
cursor.executemany("""
    INSERT INTO banks (bank_id, bank_name) VALUES (:1, :2)
""", [(idx, name) for name, idx in banks.items()])

# Insert reviews
for idx, row in df.iterrows():
    cursor.execute("""
        INSERT INTO reviews (
            review_id, bank_id, review_text, rating, date_posted, sentiment, theme
        ) VALUES (
            :1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'), :6, :7
        )
    """, (
        idx + 1,
        banks[row['bank']],
        row['review'],
        int(row['rating']),
        str(row['date']),
        row['sentiment'],
        row['theme']
    ))

connection.commit()
cursor.close()
connection.close()
print("✅ Data inserted into Oracle DB")
