import pytest
from src.lead_scorer import score_lead

def test_score_lead_valid_email():
    lead = {
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'title': 'CEO',
        'company': 'Example Corp',
        'linkedin': 'https://linkedin.com/in/johndoe'
    }
    assert score_lead(lead) == 100

def test_score_lead_invalid_email():
    lead = {
        'name': 'Jane Smith',
        'email': 'jane.smith@gmail.com',
        'title': 'Manager',
        'company': 'Example Corp',
        'linkedin': 'https://linkedin.com/in/janesmith'
    }
    assert score_lead(lead) == 70

def test_score_lead_no_linkedin():
    lead = {
        'name': 'Alice Johnson',
        'email': 'alice.johnson@company.com',
        'title': 'CTO',
        'company': 'Company Inc',
        'linkedin': ''
    }
    assert score_lead(lead) == 80

def test_score_lead_generic_email():
    lead = {
        'name': 'Bob Brown',
        'email': 'bob.brown@yahoo.com',
        'title': 'Founder',
        'company': 'Startup LLC',
        'linkedin': 'https://linkedin.com/in/bobbrown'
    }
    assert score_lead(lead) == 60

def test_score_lead_company_domain_match():
    lead = {
        'name': 'Charlie Black',
        'email': 'charlie.black@company.com',
        'title': 'Manager',
        'company': 'Company Inc',
        'linkedin': 'https://linkedin.com/in/charlieblack'
    }
    assert score_lead(lead) == 90