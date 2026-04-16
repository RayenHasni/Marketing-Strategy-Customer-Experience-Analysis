import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import scipy


model_name = "cardiffnlp/twitter-roberta-base-sentiment"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

labels = ["negative", "neutral", "positive"]

def analyze_comment(text):
    '''Function to predict sentiment + rating'''

    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    output = model(**inputs)
    scores = output[0][0].detach().numpy()
    scores = scipy.special.softmax(scores)    
    sentiment = labels[scores.argmax()]
    
    return sentiment


def apply_roberta(df: pd.DataFrame):
    
    result = df.copy()
    result["sentiment"] = result['ReviewText'].apply(analyze_comment)

    return result