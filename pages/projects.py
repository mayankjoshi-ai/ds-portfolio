def show_page():
    import streamlit as st

    st.title("Projects by Domain")
    domain = st.selectbox("Select a Domain:", ["Retail", "Sports", "Real Estate", "Healthcare"])
    theme = st.radio("Select a Theme:", ["LLM Applications", "Predictive Analytics", "Dashboards"])

    st.markdown(f"### Projects in {domain} ({theme})")
    projects = {
        "Retail": ["Customer Segmentation", "Sales Forecasting"],
        "Sports": ["Player Performance Prediction", "Fan Sentiment Analysis"],
        "Real Estate": ["Price Prediction", "Demand Analysis"],
        "Healthcare": ["Disease Diagnosis", "Patient Analytics"],
    }
    for project in projects.get(domain, []):
        st.markdown(f"- **{project}**")
        st.button(f"View {project}")