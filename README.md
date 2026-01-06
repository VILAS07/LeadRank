# 📊 LeadRank - Smart Lead Scoring System

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.24.0-FF4B4B.svg)](https://streamlit.io)

## 🎯 Overview
LeadRank is an intelligent lead scoring and analytics platform that helps sales teams prioritize their most promising leads. Using advanced algorithms and customizable criteria, it automatically scores and segments leads based on multiple factors including email validity, job seniority, and domain quality.

## ✨ Key Features
- **Smart Lead Scoring**
  - Automated scoring based on multiple weighted criteria
  - Customizable scoring parameters
  - Real-time score calculation

- **Advanced Analytics**
  - Interactive dashboards with key metrics
  - Lead quality indicators
  - Visual insights with charts and graphs
  - Word cloud analysis of job titles

- **Intelligent Filtering**
  - Score-based filtering
  - Job level categorization (CXO, VP, Director, etc.)
  - Email domain type analysis
  - Custom filter combinations

- **Data Validation**
  - Email format verification
  - Domain analysis
  - LinkedIn URL validation
  - Company domain matching

- **Export Options**
  - CSV export
  - Excel export
  - Filtered results download

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- Git

### Installation
1. Clone the repository:
```powershell
git clone https://github.com/VILAS07/LeadRank.git
cd LeadRank
```

2. Create and activate virtual environment:
```powershell
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```powershell
pip install -r requirements.txt
```

### Running the App
```powershell
streamlit run src/app.py
```

## 📖 Usage Guide

### 1. Data Preparation
Prepare your CSV file with these columns:
- `email`: Email address
- `title`: Job title
- `company`: Company name
- `linkedin`: LinkedIn profile URL

### 2. Scoring Criteria
Leads are scored based on:
- Email validity (40 points)
- Job title seniority (20 points)
- Email domain quality (20 points)
- LinkedIn presence (10 points)
- Company domain match (10 points)

### 3. Using the Dashboard
1. **Upload Data**: Use the file uploader to import your leads
2. **Configure Weights**: Adjust scoring weights in the sidebar
3. **Filter Results**: Use the advanced filtering options
4. **Analyze Insights**: Explore the analytics dashboard
5. **Export Results**: Download processed data in preferred format

## 📊 Sample Data
Generate sample data for testing:
```powershel
python src/a.py
```

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License
[MIT](https://choosealicense.com/licenses/mit/)

## 📬 Contact
Vilas - [@VILAS07](https://github.com/VILAS07)

Project Link: [https://github.com/VILAS07/LeadRank](https://github.com/VILAS07/LeadRank)
