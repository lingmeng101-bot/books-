import sqlite3

import pandas as pd

import config


def main():
    conn = sqlite3.connect(config.DB_NAME)
    df = pd.read_sql("SELECT * FROM XIA_XUN", conn)
    conn.close()


    df["price"] = df["price"].str.strip("£ ")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["star"] = df["star"].fillna(0).astype(int)
    df["stock"] = df["stock"].str.strip()

    df.to_csv(config.DATA_DIR / "books_clean.csv", index=False, encoding="utf-8-sig")
    print(f"导出 {len(df)} 行到 books_clean.csv")

if __name__ == "__main__":
    main()