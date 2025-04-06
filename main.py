import streamlit as st
from streamlit_option_menu import option_menu
from pages import introduction, projects, contact, blog
from utils.style import load_css

def main():
    st.set_page_config(page_title="Data Science Portfolio", layout="wide", page_icon='⚔️', initial_sidebar_state='expanded')
    load_css()

    st.markdown(
        """
        <style>
        [data-testid="stSidebarNav"] { display: none; } /* Hides the default pages directory listing */
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Navigation Bar
    with st.sidebar:
        st.image("images/mayank_pic.jpg", caption="AI Scientist", use_container_width=True)
        selected = option_menu(
            menu_title="Main Menu",
            # options=["Home", "Projects", "Blog", "Contact"],
            # icons=["house", "list-task", "tools", "book", "envelope"],
            options=["Home", "Blog", "Contact"],
            icons=["house", "book", "envelope"],
            menu_icon="cast",
            default_index=0,
        )

    # Page Selection
    if selected == "Home":
        introduction.show_page()
    # elif selected == "Projects":
    #     projects.show_page()
    elif selected == "Contact":
        contact.show_page()
    elif selected == "Blog":
        blog.show_page()

if __name__ == "__main__":
    main()
    st.markdown("---")
    st.markdown("<p style='text-align: center'>Copyright © 2025 Mayank Joshi. All rights reserved.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center'>Created by Mayank Joshi</p>", unsafe_allow_html=True)