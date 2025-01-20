def show_page():
    import streamlit as st

    st.title("Contact Me")
    with st.form(key="contact_form"):
        name = st.text_input("Your Name:")
        email = st.text_input("Your Email:")
        message = st.text_area("Your Message:")
        submit_button = st.form_submit_button(label="Send")
        if submit_button:
            st.success("Message Sent Successfully!")