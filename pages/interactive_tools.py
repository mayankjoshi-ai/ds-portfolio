def show_page():
    import streamlit as st
    import pandas as pd
    import plotly.express as px

    st.title("Data Science Projects")
    tab1, tab2 , tab3 = st.tabs(['Predictive Analytics', 'Gen AI' , 'Data Visualization'])
    with tab1:
        st.markdown("### Predictive Analytics Tool")
        user_input = st.slider("Input a value:", 0, 100, 50)
        st.write(f"Predicted Value: {user_input * 2}")
    with tab2:
        st.markdown("### LLM Chatbot")
        user_query = st.text_input("Ask something:")
        if user_query:
            st.write(f"Chatbot Response: '{user_query}' is a great question!")
    with tab3:
        st.markdown("### Dashboard")
        sample_data = pd.DataFrame({"Category": ["A", "B", "C"], "Values": [10, 20, 30]})
        fig = px.bar(sample_data, x="Category", y="Values", title="Sample Dashboard")
        st.plotly_chart(fig)