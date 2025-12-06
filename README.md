# Marketing Strategy & Customer Experience Analysis

## Overview

**ShopEasy**, an online retail business, faced declining customer engagement and conversion rates despite investing in multiple marketing campaigns. This project analyzes customer behavior, engagement patterns, and product performance to identify root causes and provide actionable recommendations. Through data extraction, sentiment analysis, and visualization, the project uncovers insights that drive marketing optimization and improve customer experience.

## Business Problem

- **Reduced Customer Engagement**: Declining interactions with marketing content and site
- **Decreased Conversion Rates**: Fewer visitors converting to paying customers
- **High Marketing Expenses**: Significant spend without proportional return on investment
- **Need for Feedback Analysis**: Understanding customer opinions to improve engagement and conversions

## Project Objectives

- **Increase Conversion Rates**: Identify conversion bottlenecks and optimize the sales funnel
- **Enhance Customer Engagement**: Determine which content types drive highest interaction
- **Improve Feedback Scores**: Analyze customer sentiment to guide product improvements
- **Extract & Integrate** multi-source customer and engagement data from SQL databases
- **Analyze Sentiment** from customer reviews to gauge satisfaction and identify pain points

## Project Structure

```
Marketing Management/
├── 1. Clean Data/              # SQL queries for data extraction
│   ├── CustomerQ.sql           # Customer demographics & geography
│   ├── EngagementQ.sql         # Customer engagement metrics
│   ├── JourneyQ.sql            # Customer journey stages
│   ├── ProductQ.sql            # Product performance data
│   └── ReviewsQ.sql            # Customer review data
├── 2. Sentiment Analysis/       # NLP-powered sentiment processing
│   ├── SentimentAnalysis.py     # VADER sentiment analysis script
│   └── customer_reviews_with_sentiment.csv  # Enriched review data with sentiment scores
└── 3. Dashboard/               # Interactive visualizations
```

## Key Technologies

- **SQL Server** – Data extraction and aggregation from relational databases
- **Python** – Sentiment analysis using NLTK VADER (1,365+ reviews processed)
- **Pandas** – Data manipulation and transformation
- **NLP** – Natural Language Processing for sentiment classification (Positive, Negative, Mixed)

## Methodology

### 1. Data Extraction
Five SQL queries aggregate customer, engagement, journey, product, and review data from normalized tables, joining customer demographics with geographic and engagement information.

### 2. Sentiment Analysis
- Implemented VADER sentiment analyzer to compute polarity scores (-1 to 1) for each review
- Created hybrid classification logic combining sentiment scores with star ratings
- Categorized reviews into: *Positive*, *Negative*, *Mixed Positive*, *Mixed Negative*

### 3. Sentiment Bucketing
Sentiment scores segmented into 5 buckets for deeper analysis:
- -1.0 to -0.5: Strong Negative
- -0.49 to 0.0: Mixed Negative
- 0.0 to 0.49: Mild Positive
- 0.5 to 1.0: Strong Positive

### 4. Visualization & Reporting
Interactive dashboard consolidates findings for marketing team to identify high-value customer segments, product strengths/weaknesses, and targeted improvement areas.

## Key Performance Indicators (KPIs)

- **Conversion Rate**: Percentage of website visitors who make a purchase
- **Customer Engagement Rate**: Level of interaction with marketing content (clicks, likes, comments)
- **Average Order Value (AOV)**: Average amount spent by a customer per transaction
- **Customer Feedback Score**: Average rating from customer reviews

## Recommended Actions

**Increase Conversion Rates**
- Target high-performing product categories (Kayaks, Ski Boots, Baseball Gloves) with seasonal promotions during peak months (January, September)
- Optimize conversion funnel by identifying and reducing visitor drop-off points

**Enhance Customer Engagement**
- Revitalize content strategy with interactive videos and user-generated content
- Optimize call-to-action placement on social media and blog content during historically lower-engagement periods (September-December)

**Improve Customer Feedback Scores**
- Address recurring mixed and negative feedback through targeted product improvements
- Implement feedback loop to follow up with dissatisfied customers and encourage re-rating toward 4.0+ target

## How to Use

1. **Run SQL Queries**: Execute queries in `1. Clean Data/` against your SQL Server database to extract clean, integrated datasets
2. **Process Sentiment**: Run `SentimentAnalysis.py` to analyze reviews and generate enriched sentiment data
3. **Build Dashboard**: Connect dashboard tools (Power BI/Tableau) to visualization layer using processed data
4. **Monitor KPIs**: Track conversion rate, engagement rate, AOV, and feedback scores monthly
- High-performing product categories identified for targeted seasonal promotions
- Geographic and demographic segmentation enables personalized marketing campaigns
- Mixed and negative sentiment themes highlight specific areas for product and service improvement


## Future Enhancements

- Deploy advanced NLP models (BERT, DistilBERT) for nuanced sentiment classification
- Implement predictive modeling for customer churn and lifetime value
- Automate pipeline with scheduling for real-time sentiment monitoring
- Expand analysis to social media and competitor reviews

## Skills Demonstrated

✓ SQL Query Optimization & Data Integration  
✓ Python Data Analysis & NLP  
✓ Sentiment Analysis & Classification  
✓ Data Visualization & Storytelling  
✓ Business Analytics & Insight Generation  

---
