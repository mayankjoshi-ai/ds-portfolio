def show_page():
    import streamlit as st
    import sys
    import os

    # Add the project_app_files directory to Python path
    project_files_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'project_app_files')
    if project_files_path not in sys.path:
        sys.path.append(project_files_path)

    # CSS for project cards
    st.markdown("""
        <style>
        .project-card {
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            border: 1px solid rgba(49, 51, 63, 0.2);
        }

        /* Button styles */
        div[data-testid="stButton"] button {
            transition: all 0.3s ease;
            width: 100%;
        }
        div[data-testid="stButton"] button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        </style>
    """, unsafe_allow_html=True)

    def project_card(title, description, domain, category, button_key, on_click=None):
        """Display a project card with title, description, and button."""
        with st.container():
            col1, col2 = st.columns([5, 1])
            
            # Project info in the left column
            with col1:
                st.subheader(title)
                st.write(description)
                st.caption(f"🏷️ {domain} | {category}")
            
            # Launch button in the right column, vertically centered
            with col2:
                st.write("")  # Add some spacing
                button_clicked = st.button("▶️ Launch", key=button_key, type="primary", use_container_width=True)
            
            if button_clicked:
                if on_click:
                    on_click()
                else:
                    st.info("Project coming soon!")
            
            # Add separator
            st.markdown("---")

    st.title("Projects Portfolio")

    # Sidebar filters
    with st.sidebar:
        st.header("🔍 Filter Projects")
        st.markdown("---")
        
        # Domain filter
        domains = ["All Domains", "Retail", "Finance", "Tech & AI", "Manufacturing", "Healthcare"]
        selected_domain = st.selectbox("🏢 Select Domain", domains)
        
        # Category filter
        categories = ["All Categories", "Data Visualization", "Predictive Models", "LLM Use Cases"]
        selected_category = st.selectbox("📊 Select Category", categories)

    # Define all projects
    def launch_sales_dashboard():
        import project_app_files.retail.data_viz.sales_insights as sales_insights
        sales_insights.show_dashboard()

    projects = [
        {
            "title": "📊 Retail Sales Analytics Dashboard",
            "description": "An endeavor in retail analytics through interactive visualization, harnessing data insights for enhanced business intelligence.",
            "domain": "Retail",
            "category": "Data Visualization",
            "key": "retail_dashboard",
            "on_click": launch_sales_dashboard
        }
    ]
    # Filter projects based on selection
    filtered_projects = projects
    if selected_domain != "All Domains":
        filtered_projects = [p for p in filtered_projects if p["domain"] == selected_domain]
    if selected_category != "All Categories":
        filtered_projects = [p for p in filtered_projects if p["category"] == selected_category]

    # Display project count
    st.caption(f"Showing {len(filtered_projects)} of {len(projects)} projects")
    
    # Display filtered projects
    for project in filtered_projects:
        project_card(
            title=project["title"],
            description=project["description"],
            domain=project["domain"],
            category=project["category"],
            button_key=project["key"],
            on_click=project["on_click"]
        )