import streamlit as st
import pandas as pd
from lead_scorer import score_lead
from email_validator import is_valid_email

def main():
    st.title("LeadRank - Smart Lead Scoring & Email Verifier")
    
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Preview of the uploaded leads:")
        st.dataframe(df)

        if st.button("Score Leads"):
            df['Email_Status'] = df['email'].apply(lambda email: "Valid" if is_valid_email(email) else "Invalid")
            df['Lead_Score'] = df.apply(score_lead, axis=1)
            st.write("Scored Leads:")
            st.dataframe(df)

            output_file = st.text_input("Enter output CSV file name (without .csv):", "scored_leads")
            if st.button("Download Scored Leads"):
                df.to_csv(f"{output_file}.csv", index=False)
                st.success(f"File {output_file}.csv has been created!")

if __name__ == "__main__":
    main()