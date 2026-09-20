# analyze.py
import pandas as pd


def main():
    df = pd.read_csv("books_clean.csv")

    print("=== 价格统计 ===")
    print(df["price"].describe())

    print("\n=== 评分分布 ===")
    print(df["star"].value_counts().sort_index())

    print("\n=== 最贵 Top 10 ===")
    print(df.nlargest(10, "price")[["book_name", "price"]].to_string(index=False))


    with pd.ExcelWriter("books_stats.xlsx", engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="all_books", index=False)
        df["price"].describe().to_frame("price").to_excel(writer, sheet_name="price_stats")
        df["star"].value_counts().sort_index().to_frame("count").to_excel(writer, sheet_name="star_dist")
        df.nlargest(10, "price")[["book_name", "price"]].to_excel(writer, sheet_name="top10", index=False)

    print("\n报表已保存到 books_stats.xlsx")

if __name__ == "__main__":
    main()