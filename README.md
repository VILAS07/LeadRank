# LeadRank - Smart Lead Scoring & Email Verifier

LeadRank is a Python application designed to read a CSV file of leads, verify email addresses, and score each lead based on defined criteria. The application aims to help users identify high-quality leads for their business.

## Features

- Validates email addresses using regex or an API.
- Scores leads based on various criteria, including job title relevance and email domain checks.
- Outputs a new CSV file with additional columns for Email Status and Lead Score.
- Optional Streamlit interface for easy file uploads and result previews.

## Project Structure

```
leadrank
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── email_validator.py
│   ├── lead_scorer.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── ui
│       ├── __init__.py
│       └── streamlit_app.py
├── tests
│   ├── __init__.py
│   ├── test_email_validator.py
│   └── test_lead_scorer.py
├── data
│   └── sample_leads.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd leadrank
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Prepare your leads in a CSV file with the following columns: `name`, `email`, `title`, `company`, `LinkedIn`.
2. Run the application:
   ```
   python src/main.py <path-to-your-leads.csv>
   ```
3. The output will be a new CSV file with the additional columns `Email_Status` and `Lead_Score`.

## Optional: Streamlit Interface

To use the Streamlit interface, run:
```
streamlit run src/ui/streamlit_app.py
```

This will allow you to upload your CSV file, preview the results, and download the scored leads.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.