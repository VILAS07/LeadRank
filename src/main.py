import pandas as pd
import re
from typing import Dict, List
import validators

def validate_email(email: str) -> bool:
    """Validate email using regex pattern."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def score_lead(row: pd.Series, weights: dict = None) -> int:
    """Calculate lead score based on defined criteria and optional weights."""
    if weights is None:
        weights = {
            'email': 40,
            'title': 20,
            'domain': 20,
            'linkedin': 10,
            'company': 10
        }
    
    score = 0
    
    # Email validation check
    if validate_email(row['email']):
        score += weights['email']
        
    # Title keywords check
    title_keywords = ['CEO', 'Founder', 'CTO', 'Manager', 'Director', 'VP', 'Head']
    if any(keyword.lower() in str(row['title']).lower() for keyword in title_keywords):
        score += weights['title']
        
    # Email domain check
    generic_domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com']
    email_domain = row['email'].split('@')[1].lower()
    if email_domain not in generic_domains:
        score += weights['domain']
        
    # LinkedIn URL check
    if pd.notna(row['linkedin']) and validators.url(str(row['linkedin'])):
        score += weights['linkedin']
        
    # Company domain match check
    if pd.notna(row['company']):
        company_name = row['company'].lower().replace(' ', '')
        if company_name in email_domain:
            score += weights['company']
            
    return score

def process_leads(input_file: str, output_file: str) -> None:
    """Process lead data and generate scored output."""
    # Read input CSV
    df = pd.read_csv(input_file)
    
    # Validate emails and add status column
    df['Email_Status'] = df['email'].apply(validate_email)
    
    # Calculate lead scores
    df['Lead_Score'] = df.apply(score_lead, axis=1)
    
    # Export results
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file = "C:/Users/vilas/Desktop/z/data/sample_leads.csv"
    output_file = "C:/Users/vilas/Desktop/z/data/scored_leads.csv"
    process_leads(input_file, output_file)