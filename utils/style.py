def load_css():
    import streamlit as st

    st.markdown(
        """<style>
        body { font-family: 'Arial', sans-serif; }
        .dark-toggle { position: absolute; top: 10px; right: 10px; }
        </style>""",
        unsafe_allow_html=True,
    )