import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
from openpyxl import Workbook
from main import validate_email, score_lead
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(
    page_title="LeadRank - Smart Lead Scoring",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTitle {
        color: #2E4057;
        font-size: 3rem !important;
    }
    .stSubheader {
        color: #048BA8;
    }
    .stMetric {
        background-color: #F7F7F7;
        padding: 1rem;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

def create_word_cloud(text):
    """Generate word cloud from text"""
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    return fig

def categorize_title(title):
    """Categorize job titles into specific levels with strict matching"""
    title = str(title).lower().strip()
    
    # Define title categories with keywords
    categories = {
        'CXO': ['ceo', 'cto', 'cfo', 'coo', 'chief', 'founder', 'president'],
        'VP': ['vp', 'vice president', 'vice-president', 'avp', 'svp', 'evp'],
        'Director': ['director', 'head of', 'lead'],
        'Manager': ['manager', 'supervisor', 'team lead'],
        'Other': []  # Default category
    }
    
    for level, keywords in categories.items():
        if any(keyword in title for keyword in keywords):
            return level
    return 'Other'

def get_email_domain_type(email):
    """Categorize email domains with more specific classifications"""
    try:
        domain = email.split('@')[1].lower()
        generic_domains = {
            'Generic': ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com', 'aol.com'],
            'Professional': ['linkedin.com', 'indeed.com'],
            'Academic': ['.edu', 'university', 'college', 'school'],
        }
        
        for domain_type, domains in generic_domains.items():
            if any(d in domain for d in domains):
                return domain_type
        return 'Corporate'
    except:
        return 'Invalid'

# Replace the filtering section in tab1 with:
def main():
    # Sidebar - Scoring Customization
    st.sidebar.title("⚙️ Scoring Settings")
    weights = {
        'email': st.sidebar.slider("Email Validity Weight", 0, 50, 40),
        'title': st.sidebar.slider("Title Weight", 0, 30, 20),
        'domain': st.sidebar.slider("Domain Weight", 0, 30, 20),
        'linkedin': st.sidebar.slider("LinkedIn Weight", 0, 20, 10),
        'company': st.sidebar.slider("Company Match Weight", 0, 20, 10)
    }

    # Header section
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("📊 LeadRank")
        st.subheader("Smart Lead Scoring System")
    with col2:
        st.image("https://img.icons8.com/clouds/200/000000/lead.png", width=150)

    # File upload section
    st.markdown("---")
    st.write("### 📁 Upload Your Leads")
    uploaded_file = st.file_uploader(
        "Upload a CSV file containing lead information",
        type="csv",
        help="File should contain columns: name, email, title, company, linkedin"
    )
    
    if uploaded_file is not None:
        # Read and process data
        df = pd.read_csv(uploaded_file)
        df['Email_Status'] = df['email'].apply(validate_email)
        df['Lead_Score'] = df.apply(lambda x: score_lead(x, weights), axis=1)
        
        # Dashboard Tabs
        tab1, tab2, tab3 = st.tabs(["📊 Scored Leads", "📈 Insights", "📋 Raw Data"])
        
        with tab1:
            st.write("### 🔍 Advanced Lead Filtering")
    
            # Create three columns for filters
            filter_col1, filter_col2, filter_col3 = st.columns(3)
    
            with filter_col1:
                # Score range filter with min/max display
                score_min, score_max = st.slider(
                    "Lead Score Range 📊",
                    min_value=0,
                    max_value=100,
                    value=(0, 100),
                    help="Filter leads by their score range"
                )
                st.caption(f"Selected range: {score_min} to {score_max}")
    
            with filter_col2:
                # Job level filter with counts
                df['Job_Level'] = df['title'].apply(categorize_title)
                level_counts = df['Job_Level'].value_counts()
                level_options = [f"{level} ({level_counts[level]})" 
                                for level in ['CXO', 'VP', 'Director', 'Manager', 'Other']
                                if level in level_counts]
                
                selected_levels = st.multiselect(
                    "Job Levels 👔",
                    options=level_options,
                    default=level_options,
                    help="Filter by job seniority level"
                )
                # Extract actual levels without counts
                selected_levels = [level.split(' (')[0] for level in selected_levels]
    
            with filter_col3:
                # Email domain type filter with counts
                df['Email_Type'] = df['email'].apply(get_email_domain_type)
                domain_counts = df['Email_Type'].value_counts()
                domain_options = [f"{domain} ({domain_counts[domain]})" 
                                for domain in domain_counts.index]
                
                selected_domains = st.multiselect(
                    "Email Domain Types 📧",
                    options=domain_options,
                    default=domain_options,
                    help="Filter by email domain type"
                )
                # Extract actual domain types without counts
                selected_domains = [domain.split(' (')[0] for domain in selected_domains]

            # Apply filters with error handling
            try:
                filtered_df = df[
                    (df['Lead_Score'].between(score_min, score_max)) &
                    (df['Job_Level'].isin(selected_levels)) &
                    (df['Email_Type'].isin(selected_domains))
                ]
                
                # Show filter summary
                st.success(f"📋 Showing {len(filtered_df)} out of {len(df)} leads")
                
                if len(filtered_df) == 0:
                    st.warning("No leads match the selected filters. Try adjusting your criteria.")
                else:
                    # Display filtered results with enhanced formatting
                    st.dataframe(
                        filtered_df,
                        column_config={
                            "Lead_Score": st.column_config.ProgressColumn(
                                "Lead Score",
                                help="Score based on multiple criteria",
                                format="%d",
                                min_value=0,
                                max_value=100,
                            ),
                            "Job_Level": st.column_config.Column(
                                "Job Level",
                                help="Categorized job level"
                            ),
                            "Email_Type": st.column_config.Column(
                                "Email Domain Type",
                                help="Type of email domain"
                            )
                        },
                        hide_index=True
                    )
            except Exception as e:
                st.error(f"Error applying filters: {str(e)}")

        with tab2:
            st.write("### 📊 Lead Intelligence Dashboard")
            
            # Key Metrics Row
            metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
            
            with metric_col1:
                avg_score = df['Lead_Score'].mean()
                st.metric("Average Lead Score", f"{avg_score:.1f}", 
                         delta=f"{avg_score - 50:.1f} vs baseline")
            
            with metric_col2:
                high_value_leads = len(df[df['Lead_Score'] >= 80])
                st.metric("High-Value Leads (80+)", high_value_leads,
                         f"{(high_value_leads/len(df))*100:.1f}% of total")
            
            with metric_col3:
                valid_emails = df['Email_Status'].sum()
                st.metric("Valid Email Rate", 
                         f"{(valid_emails/len(df))*100:.1f}%",
                         f"{valid_emails} of {len(df)}")
            
            with metric_col4:
                corporate_emails = len(df[df['Email_Type'] == 'Corporate'])
                st.metric("Corporate Email Rate",
                         f"{(corporate_emails/len(df))*100:.1f}%",
                         f"{corporate_emails} of {len(df)}")

            st.markdown("---")

            # Detailed Analytics
            col1, col2 = st.columns(2)
            
            with col1:
                # Score Distribution
                fig_score = px.histogram(
                    df, 
                    x="Lead_Score",
                    title="Lead Score Distribution",
                    nbins=20,
                    color_discrete_sequence=['#2E4057']
                )
                fig_score.update_layout(showlegend=False)
                st.plotly_chart(fig_score, use_container_width=True)
                
                # Job Level Distribution
                job_level_dist = df['Job_Level'].value_counts()
                fig_job = px.pie(
                    values=job_level_dist.values,
                    names=job_level_dist.index,
                    title="Job Level Distribution",
                    color_discrete_sequence=px.colors.qualitative.Set3
                )
                st.plotly_chart(fig_job, use_container_width=True)

            with col2:
                # Email Domain Analysis
                email_type_dist = df['Email_Type'].value_counts()
                fig_email = px.pie(
                    values=email_type_dist.values,
                    names=email_type_dist.index,
                    title="Email Domain Distribution",
                    hole=0.4,
                    color_discrete_sequence=px.colors.qualitative.Pastel
                )
                st.plotly_chart(fig_email, use_container_width=True)
                
                # Job Title Word Cloud
                if 'title' in df.columns:
                    st.write("### 🔤 Job Title Word Cloud")
                    titles_text = ' '.join(df['title'].dropna())
                    st.pyplot(create_word_cloud(titles_text))

            # Lead Quality Gauge
            st.markdown("---")
            st.write("### 📈 Lead Quality Indicators")
            gauge_col1, gauge_col2, gauge_col3 = st.columns(3)
            
            with gauge_col1:
                # Overall Quality Score
                quality_score = (avg_score + (corporate_emails/len(df))*100)/2
                st.plotly_chart(
                    create_gauge_chart(quality_score, "Overall Lead Quality"),
                    use_container_width=True
                )
            
            with gauge_col2:
                # Seniority Mix
                seniority_score = (len(df[df['Job_Level'].isin(['CXO', 'VP', 'Director'])])/len(df))*100
                st.plotly_chart(
                    create_gauge_chart(seniority_score, "Seniority Mix"),
                    use_container_width=True
                )
            
            with gauge_col3:
                # Email Quality
                email_quality = (valid_emails/len(df))*100
                st.plotly_chart(
                    create_gauge_chart(email_quality, "Email Quality"),
                    use_container_width=True
                )

            # Add correlation analysis if numerical columns exist
            st.markdown("---")
            st.write("### 🔍 Additional Insights")
            
            # Display top domains
            st.write("#### Top Email Domains")
            email_domains = df['email'].apply(lambda x: x.split('@')[1] if '@' in str(x) else 'Invalid')
            st.dataframe(
                email_domains.value_counts().head(10).reset_index(),
                column_config={
                    "index": "Domain",
                    "email": "Count"
                },
                hide_index=True
            )

        with tab3:
            st.write("### Original Data")
            st.dataframe(df, hide_index=True)

        # Export Options
        st.markdown("---")
        st.write("### 📤 Export Options")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # CSV Export
            st.download_button(
                "📥 Download CSV",
                data=df.to_csv(index=False),
                file_name="scored_leads.csv",
                mime="text/csv"
            )
        
        with col2:
            # Excel Export
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                df.to_excel(writer, index=False)
            st.download_button(
                "📊 Download Excel",
                data=buffer.getvalue(),
                file_name="scored_leads.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        
        with col3:
            # Google Sheets Integration (placeholder)
            st.button("☁️ Export to Google Sheets", disabled=True, 
                     help="Coming soon!")

def create_gauge_chart(value, title):
    """Create a gauge chart using plotly"""
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = value,
        title = {'text': title},
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': "#2E4057"},
            'steps': [
                {'range': [0, 40], 'color': "#FF9B9B"},
                {'range': [40, 70], 'color': "#FFD89B"},
                {'range': [70, 100], 'color': "#B5F1CC"}
            ]
        }
    ))
    return fig

if __name__ == "__main__":
    main()