from DataIngestion import fetch_data_from_csv, fetch_data_from_sql
from RobertaAnalyzer import apply_roberta

from pathlib import Path


SOURCE = "sql"
OUTPUT_PATH = "output/customer_reviews_with_sentiment.csv"


def load_reviews(source: str):
    if source == "sql":
        return fetch_data_from_sql(
            server="DESKTOP-BDE04OR\\SQLEXPRESS",
            database="PortfolioProject_MarketingAnalytics",
            query="SELECT * FROM dbo.customer_reviews",
        )

    if source == "csv":
        return fetch_data_from_csv("customer_reviews.csv")

    raise ValueError("SOURCE must be 'sql' or 'csv'.")


def main() -> None:
    reviews_df = load_reviews(SOURCE)
    enriched_df = apply_roberta(reviews_df)
    Path("output").mkdir(parents=True, exist_ok=True)

    enriched_df.to_csv(OUTPUT_PATH, index=False)


if __name__ == "__main__":
    main()