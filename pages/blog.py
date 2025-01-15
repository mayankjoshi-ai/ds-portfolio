def show_page():
    import streamlit as st

    st.title("Blog")
    st.markdown("### Latest Posts")
    blogs = [
        "Understanding LLMs: A Beginner's Guide",
        "How Predictive Analytics Transforms Business",
        "Building Dashboards with Streamlit: Best Practices",
    ]
    for blog in blogs:
        st.markdown(f"- {blog}")