def score_lead(lead: dict) -> int:
    score = 0

    # Check if email is valid
    if is_valid_email(lead['email']):
        score += 40

    # Check if title contains keywords
    keywords = ["CEO", "Founder", "CTO", "Manager"]
    if any(keyword in lead['title'] for keyword in keywords):
        score += 20

    # Check if email domain is not generic
    generic_domains = ["gmail.com", "yahoo.com", "outlook.com"]
    email_domain = lead['email'].split('@')[-1]
    if email_domain not in generic_domains:
        score += 20

    # Check if LinkedIn URL is present
    if lead.get('LinkedIn'):
        score += 10

    # Check if email domain matches company domain
    company_domain = lead['company'].split()[-1].lower() + ".com"  # Simplistic approach
    if email_domain == company_domain:
        score += 10

    return score