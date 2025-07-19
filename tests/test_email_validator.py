import pytest
from src.email_validator import is_valid_email

def test_valid_email():
    assert is_valid_email("test@example.com") == True
    assert is_valid_email("user.name+tag+sorting@example.com") == True
    assert is_valid_email("user@subdomain.example.com") == True

def test_invalid_email():
    assert is_valid_email("plainaddress") == False
    assert is_valid_email("@missingusername.com") == False
    assert is_valid_email("username@.com") == False
    assert is_valid_email("username@domain..com") == False