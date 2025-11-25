import pandas as pd
import pyodbc
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


nltk.download('vader_lexicon')

def fetch_data_from_sql():
 conn_str = (
   "Driver={SQL Server};"
   "Server=DESKTOP-BDE04OR\SQLEXPRESS;"
   "Database=PortfolioProject_MarketingAnalytics;"
    "Trusted_Connection=yes;")
 conn = pyodbc.connect(conn_str)

 query = "SELECT * FROM dbo.customer_reviews"

 df = pd.read_sql(query, conn)

 conn.close()

 return df


customers_reviews = fetch_data_from_sql()

sia = SentimentIntensityAnalyzer()

def calculate_sentiment(review):
    return sia.polarity_scores(review)['compound']

def categorize_sentiment(score,rating):
    if score > 0.05:
        if rating >=4:
            return 'Positive'
        elif rating ==3:
            return 'Mixed Positive'
        else:
            return 'Mixed Negative'
    elif score < -0.05:
        if rating <=2:
            return 'Negative'
        elif rating ==3:
            return 'Mixed Negative'
        else:
            return 'Mixed Positive'
    else:
        if rating >=4:
            return 'Positive'
        elif rating <=2:
            return 'Negative'
        else:
            return 'Neutral'

def sentiment_bucket(score):
    if score > 0.5:
        return '0.5 to 1.0' # Positive
    elif 0.0 <= score < 0.5: 
        return '0.0 to 0.49' # Miidly Positive
    elif -0.5 < score < 0.0:
        return '-0.49 to 0.0' # Mildly Negative
    else:
        return '-1.0 to -0.5' # Negative


# Apply the functions to the data

customers_reviews['sentimentScore'] = customers_reviews['ReviewText'].apply(calculate_sentiment)

customers_reviews['sentimentCategory'] = customers_reviews.apply(lambda x: categorize_sentiment(x['sentimentScore'], x['Rating']), axis=1)

customers_reviews['sentimentBucket'] = customers_reviews['sentimentScore'].apply(sentiment_bucket)

# repalce double spaces with single space in the ReviewText column
customers_reviews['ReviewText'] = customers_reviews['ReviewText'].str.replace('\s+', ' ', regex=True)

print(customers_reviews.head())

# Save the data to a csv file
customers_reviews.to_csv('customer_reviews_with_sentiment.csv', index=False)