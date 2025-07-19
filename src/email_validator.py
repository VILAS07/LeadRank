def is_valid_email(email: str) -> bool:
    import re

    # Basic regex for validating an email
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Check if the email matches the regex
    if re.match(regex, email):
        return True
    return False