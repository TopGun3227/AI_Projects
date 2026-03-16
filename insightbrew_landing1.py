#Refer St_test.py for setup instructions
#(.venv) C:\Users\abhishek.ganguly\TopGun3227Repo\AI_Projects>streamlit run "C:\Users\abhishek.ganguly\TopGun3227Repo\AI_Projects\InsightBrew\insightbrew_landing1.py"
# Reference: https://github.com/Sven-Bo/streamlit-multipage-app-example
#Local URL: http://localhost:8501
#Network URL: http://192.168.1.8:8501
# Enhanced with Colorful Designs - 2026-03-16

import streamlit as st
import pandas as pd
import numpy as np

# Page config
st.set_page_config(
    page_title="InsightBrew",
    page_icon="📊",
    layout="wide"
)

# -------- PREMIUM CSS WITH COLORFUL DESIGNS --------

st.markdown("""
<style>

.main-title {
    font-size:60px;
    font-weight:700;
    text-align:center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 20px;
}

.subtitle {
    font-size:24px;
    text-align:center;
    color: #4CAF50;
    font-weight: 500;
    margin: 10px 0;
}

.hero {
    padding:80px 20px;
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
    border-radius: 20px;
    margin: 20px 0;
    border: 2px solid rgba(102, 126, 234, 0.3);
}

.metric-card {
    padding:20px;
    border-radius:15px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    box-shadow: 0 8px 16px rgba(102, 126, 234, 0.3);
    border: none;
}

.service-card {
    padding: 30px;
    border-radius: 15px;
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    color: white;
    margin: 15px 0;
    box-shadow: 0 8px 16px rgba(245, 87, 108, 0.3);
}

.service-card-alt {
    padding: 30px;
    border-radius: 15px;
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    color: white;
    margin: 15px 0;
    box-shadow: 0 8px 16px rgba(79, 172, 254, 0.3);
}

.service-card-alt2 {
    padding: 30px;
    border-radius: 15px;
    background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
    color: white;
    margin: 15px 0;
    box-shadow: 0 8px 16px rgba(67, 233, 123, 0.3);
}

.case-study-box {
    padding: 25px;
    border-left: 5px solid #667eea;
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
    border-radius: 10px;
    margin: 20px 0;
}

.insight-box {
    padding: 25px;
    border-radius: 10px;
    background: linear-gradient(135deg, rgba(79, 172, 254, 0.15) 0%, rgba(0, 242, 254, 0.15) 100%);
    border-left: 5px solid #4facfe;
    margin: 20px 0;
}

.footer-text {
    color: #667eea;
    font-weight: 600;
}

h3 {
    margin: 0;
    color: white;
}

p {
    margin: 10px 0 0 0;
    line-height: 1.8;
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

    with col1:
        st.metric("Projects Delivered","60+")
    with col2:
        st.metric("Analytics Platforms","25+")
    with col3:
        st.metric("AI Solutions","40+")
    with col4:
        st.metric("Industries","10+")

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
        st.markdown("""
        <div class="service-card">
        <h3>📊 Data Strategy</h3>
        <p>
        • Enterprise Data Strategy<br>
        • Data Governance<br>
        • Modern Data Architecture<br>
        • Cloud Data Platforms
        </p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="service-card-alt">
        <h3>🤖 AI & Machine Learning</h3>
        <p>
        • Predictive Analytics<br>
        • ML Models<br>
        • LLM Applications<br>
        • AI Agents for Analytics
        </p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="service-card-alt2">
        <h3>📈 Analytics Products</h3>
        <p>
        • AI Analytics Apps<br>
        • Embedded Analytics<br>
        • Decision Intelligence Platforms<br>
        • Data APIs
        </p>
        </div>
        """, unsafe_allow_html=True)

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

    st.markdown("""
    <div class="case-study-box">
    <h3>🎯 Retail Demand Forecasting</h3>
    <p>Built an AI-driven demand forecasting system improving supply chain efficiency by 25%.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="case-study-box">
    <h3>🏢 Enterprise Data Platform</h3>
    <p>Designed a modern lakehouse architecture enabling real-time analytics across business units.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="case-study-box">
    <h3>👥 AI Customer Intelligence</h3>
    <p>Developed ML models to predict customer churn and improve retention strategies.</p>
    </div>
    """, unsafe_allow_html=True)

# -------- INSIGHTS --------

elif menu == "Insights":

    st.title("Insights")

    st.markdown("""
    <div class="insight-box">
    <h3>🚀 The Future of AI-Powered Analytics</h3>
    <p>AI agents are transforming how businesses interact with data and generate insights.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="insight-box">
    <h3>🔧 Building the Modern Data Stack</h3>
    <p>Architectural principles for scalable analytics platforms.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="insight-box">
    <h3>💡 Why Decision Intelligence is the Next Frontier</h3>
    <p>Moving beyond dashboards to automated insights.</p>
    </div>
    """, unsafe_allow_html=True)

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
<span class="footer-text">© 2026 InsightBrew | Data Analytics & AI Advisory</span>
</div>
""", unsafe_allow_html=True)
