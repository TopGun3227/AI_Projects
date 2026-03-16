#Refer St_test.py for setup instructions
#(.venv) C:\Users\abhishek.ganguly\TopGun3227Repo\AI_Projects>streamlit run "C:\Users\abhishek.ganguly\TopGun3227Repo\AI_Projects\InsightBrew\insightbrew_landing.py"
# Reference: https://github.com/Sven-Bo/streamlit-multipage-app-example
#Local URL: http://localhost:8501
#Network URL: http://192.168.1.8:8501


import streamlit as st
import pandas as pd
import numpy as np

# Page config
st.set_page_config(
    page_title="InsightBrew",
    page_icon="📊",
    layout="wide"
)

# -------- PREMIUM CSS --------

st.markdown("""
<style>

.main-title {
font-size:60px;
font-weight:700;
text-align:center;
}

.subtitle {
font-size:24px;
text-align:center;
color:gray;
}

.hero {
padding:80px 20px;
}

.metric-card {
padding:20px;
border-radius:10px;
background:#111;
}

</style>
""", unsafe_allow_html=True)

# -------- NAVIGATION --------

menu = st.sidebar.radio(
"Navigation",
["Home","Services","AI Demo","Case Studies","Insights","Contact"]
)

# -------- HERO SECTION --------

if menu == "Home":

    st.markdown("""
    <div class="hero">
    <div class="main-title">InsightBrew</div>
    <div class="subtitle">Brewing Powerful Insights from Data</div>
    <div class="subtitle">Data Strategy • AI Solutions • Analytics Products</div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("Projects Delivered","60+")
    col2.metric("Analytics Platforms","25+")
    col3.metric("AI Solutions","40+")
    col4.metric("Industries","10+")

    st.divider()

    st.header("Who We Are")

    st.write("""
InsightBrew is a next-generation **data analytics and AI advisory firm** that helps organizations turn complex data into strategic advantage.

We combine **modern data platforms, AI technologies, and deep analytics expertise** to help enterprises unlock the full value of their data.

From designing enterprise data architectures to building intelligent analytics products, InsightBrew helps organizations move from **data chaos to decision intelligence**.
""")

# -------- SERVICES --------

elif menu == "Services":

    st.title("Services")

    c1,c2,c3 = st.columns(3)

    with c1:
        st.subheader("Data Strategy")
        st.write("""
- Enterprise Data Strategy  
- Data Governance  
- Modern Data Architecture  
- Cloud Data Platforms
""")

    with c2:
        st.subheader("AI & Machine Learning")

        st.write("""
- Predictive Analytics  
- ML Models  
- LLM Applications  
- AI Agents for Analytics
""")

    with c3:
        st.subheader("Analytics Products")

        st.write("""
- AI Analytics Apps  
- Embedded Analytics  
- Decision Intelligence Platforms  
- Data APIs
""")

# -------- AI DEMO --------

elif menu == "AI Demo":

    st.title("AI Data Analyst Demo")

    st.write("Upload a dataset and ask questions about your data.")

    uploaded = st.file_uploader("Upload CSV")

    if uploaded:

        df = pd.read_csv(uploaded)

        st.dataframe(df)

        question = st.text_input("Ask a question about the data")

        if question:

            st.info("AI Insight (demo)")

            st.write("Dataset has", df.shape[0], "rows and", df.shape[1], "columns.")

            st.bar_chart(df.select_dtypes(include=np.number))

# -------- CASE STUDIES --------

elif menu == "Case Studies":

    st.title("Case Studies")

    st.subheader("Retail Demand Forecasting")

    st.write("""
Built an AI-driven demand forecasting system improving supply chain efficiency by 25%.
""")

    st.subheader("Enterprise Data Platform")

    st.write("""
Designed a modern lakehouse architecture enabling real-time analytics across business units.
""")

    st.subheader("AI Customer Intelligence")

    st.write("""
Developed ML models to predict customer churn and improve retention strategies.
""")

# -------- INSIGHTS --------

elif menu == "Insights":

    st.title("Insights")

    st.markdown("""
### The Future of AI-Powered Analytics

AI agents are transforming how businesses interact with data and generate insights.

### Building the Modern Data Stack

Architectural principles for scalable analytics platforms.

### Why Decision Intelligence is the Next Frontier

Moving beyond dashboards to automated insights.
""")

# -------- CONTACT --------

elif menu == "Contact":

    st.title("Contact InsightBrew")

    with st.form("contact"):

        name = st.text_input("Name")

        email = st.text_input("Email")

        company = st.text_input("Company")

        message = st.text_area("Message")

        submit = st.form_submit_button("Submit")

        if submit:

            st.success("Thank you. Our team will contact you soon.")

# -------- FOOTER --------

st.divider()

st.markdown("""
<div style="text-align:center">
© 2026 InsightBrew | Data Analytics & AI Advisory
</div>
""", unsafe_allow_html=True)