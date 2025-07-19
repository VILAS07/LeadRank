# LeadRank - Smart Lead Scoring System

## Overview
LeadRank is a powerful lead scoring and email verification system built with Python and Streamlit. It helps sales teams prioritize leads by scoring them based on multiple criteria and provides insightful analytics.

## Features
- 📊 Smart lead scoring based on multiple criteria
- ✉️ Email validation and domain analysis
- 👔 Job title categorization
- 📈 Interactive dashboards and insights
- 🔍 Advanced filtering capabilities
- 📤 Multiple export options

## Installation
1. Clone the repository:
```bash
git clone https://github.com/VILAS07/LeadRank.git
cd LeadRank
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. Start the Streamlit app:
```bash
streamlit run src/app.py
```

2. Upload your CSV file containing leads data with columns:
   - name
   - email
   - title
   - company
   - linkedin

3. Use the interactive dashboard to:
   - Score leads
   - Filter and segment data
   - Analyze insights
   - Export results

## License
MIT License