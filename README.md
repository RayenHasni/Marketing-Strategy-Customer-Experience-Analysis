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
├── 1. Business Case.pptx                    # Project overview & stakeholder presentation
├── 2. Findings Presentation.pptx            # Key insights & recommendations
├── 1. Clean Data/                           # SQL queries for data extraction
│   ├── CustomerQ.sql                        # Customer demographics & geography
│   ├── EngagementQ.sql                      # Customer engagement metrics
│   ├── JourneyQ.sql                         # Customer journey stages
│   ├── ProductQ.sql                         # Product performance data
│   └── ReviewsQ.sql                         # Customer review data
├── 2. Sentiment Analysis/                   # Advanced NLP sentiment processing
│   ├── DataIngestion.py                     # SQL & CSV data retrieval
│   ├── RobertaAnalyzer.py                   # RoBERTa transformer-based sentiment analysis
│   ├── requirements.txt                     # Python dependencies
│   ├── customer_reviews_with_sentiment.csv  # Input review data
│   └── output/                              # Enriched data with sentiment scores
└── 3. Dashboard/
    └── Marketing_Report.pbix                # Power BI interactive dashboard
```

## Key Technologies

- **SQL Server** – Data extraction and aggregation from relational databases
- **Python** – Advanced NLP sentiment analysis using transformer models (RoBERTa)
- **Transformers** – HuggingFace pretrained models for state-of-the-art NLP
- **SQLAlchemy** – Database connectivity and query execution
- **Pandas** – Data manipulation and transformation
- **Power BI** – Interactive dashboards and KPI visualizations
- **NLP** – Natural Language Processing for sentiment classification (Positive, Neutral, Negative)

## Methodology

### 1. Data Extraction
Five SQL queries aggregate customer, engagement, journey, product, and review data from normalized tables, joining customer demographics with geographic and engagement information.

### 2. Sentiment Analysis
- Implemented advanced **RoBERTa transformer model** (cardiffnlp/twitter-roberta-base-sentiment) for nuanced sentiment classification
- Built data ingestion pipeline (`DataIngestion.py`) for direct SQL and CSV connectivity
- Processed 1,365+ customer reviews with multi-label sentiment prediction
- Achieved 3-class classification: *Positive*, *Neutral*, *Negative* with confidence scores
- Optimized for social media text and concise customer feedback

### 3. Sentiment Bucketing
Sentiment predictions categorized into buckets for business analysis:
- **Positive**: Strong satisfaction signals (product praise, recommender intent)
- **Neutral**: Mixed or factual feedback (feature descriptions, comparisons)
- **Negative**: Pain points and complaints (defects, delays, service issues)
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

### For Data Analysts

1. **Review Business Context**: Open `1. Business Case.pptx` for project scope and objectives
2. **Extract Data**: 
   - Execute SQL queries in `1. Clean Data/` against your SQL Server database
   - Queries integrate customer, engagement, journey, product, and review data
3. **Process Sentiment**: 
   - Install dependencies: `pip install -r 2. Sentiment\ Analysis/requirements.txt`
   - Run `RobertaAnalyzer.py` to process reviews with RoBERTa model
   - Output enriched CSV with sentiment predictions in `2. Sentiment Analysis/output/`
4. **Build Dashboard**: 
   - Open `3. Dashboard/Marketing_Report.pbix` in Power BI
   - Connect to processed CSV outputs for live visualizations
5. **Stakeholder Communication**: Use `2. Findings Presentation.pptx` to present key insights

### For Technical Setup

```bash
# Create virtual environment (recommended)
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run sentiment analysis
python RobertaAnalyzer.py
```


## Future Enhancements

- **Pipeline Automation**: Schedule daily sentiment analysis runs with SQL triggers and Python scheduling (APScheduler)
- **Advanced Classification**: Fine-tune RoBERTa on domain-specific customer review data for improved accuracy
- **Real-time Monitoring**: Implement streaming sentiment analysis for immediate alert on negative reviews
- **Aspect-based Analysis**: Extract specific product/service features from reviews (e.g., "shipping delays", "quality issues")
- **Comparative Analysis**: Benchmark sentiment trends against competitor reviews from social media
- **Expanded Platforms**: Extend sentiment analysis to social media mentions, email feedback, and support tickets

---

**Project Status**: Complete with Advanced NLP & BI Integration  
**Last Updated**: April 2026
