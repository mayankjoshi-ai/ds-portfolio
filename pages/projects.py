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

        /* Tab styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
        }

        .stTabs [data-baseweb="tab"] {
            padding: 8px 16px;
            border-radius: 4px;
        }
        </style>
    """, unsafe_allow_html=True)

    def project_card(title, description, button_key, on_click=None):
        """Display a project card with title, description, and button."""
        with st.container():
            col1, col2 = st.columns([5, 1])
            
            # Project info in the left column
            with col1:
                st.subheader(title)
                st.write(description)
            
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
    
    # Create tabs for each domain
    retail_tab, finance_tab, tech_tab, manufacturing_tab, healthcare_tab, other_tab = st.tabs([
        "🛍️ Retail", 
        "💰 Finance", 
        "🤖 Tech & AI",
        "🏭 Manufacturing",
        "🏥 Healthcare",
        "🔄 Other"
    ])
    
    with retail_tab:
        viz_tab, pred_tab, llm_tab = st.tabs(["📊 Data Visualization", "🔮 Predictive Models", "🤖 LLM Use Cases"])
        
        with viz_tab:
            def launch_dashboard():
                import project_app_files.retail.data_viz.sales_insights as sales_insights
                sales_insights.show_dashboard()

            project_card(
                "📊 Retail Sales Analytics Dashboard",
                "An endeavor in retail analytics through interactive visualization, harnessing data insights for enhanced business intelligence.",
                "retail_dashboard",
                launch_dashboard
            )
        
        with pred_tab:
            def launch_customer_insights():
                import project_app_files.retail.data_viz.customer_insights as customer_insights
                customer_insights.show_dashboard()

            project_card(
                "🎯 Customer Insights & Campaign Platform",
                "A modular analytics solution that aggregates customer data from multiple sources to drive targeted campaigns. Enabled reactivation of lost customers and increased purchase frequency through data-driven promotions across 30+ brands, generating $2M+ in additional sales. The platform provides both quick and detailed customer analytics views, empowering brands with actionable insights for informed decision-making.",
                "customer_insights",
                launch_customer_insights
            )

            project_card(
                "👥 Customer Churn Analytics",
                "An endeavor in customer churn prediction through logistic regression, harnessing data science for enhanced customer retention.",
                "churn_analytics"
            )
        
        with llm_tab:
            project_card(
                "🤖 Retail Chat Assistant",
                "An intelligent chatbot leveraging LLMs to provide customer support and product recommendations.",
                "retail_chat"
            )

    with finance_tab:
        viz_tab, pred_tab, llm_tab = st.tabs(["📊 Data Visualization", "🔮 Predictive Models", "🤖 LLM Use Cases"])
        for tab in [viz_tab, pred_tab, llm_tab]:
            with tab:
                st.info("Finance analytics projects coming soon!")

    with tech_tab:
        viz_tab, pred_tab, llm_tab = st.tabs(["📊 Data Visualization", "🔮 Predictive Models", "🤖 LLM Use Cases"])
        for tab in [viz_tab, pred_tab, llm_tab]:
            with tab:
                st.info("Technology and AI projects coming soon!")

    with manufacturing_tab:
        viz_tab, pred_tab, llm_tab = st.tabs(["📊 Data Visualization", "🔮 Predictive Models", "🤖 LLM Use Cases"])
        for tab in [viz_tab, pred_tab, llm_tab]:
            with tab:
                st.info("Manufacturing analytics projects coming soon!")

    with healthcare_tab:
        viz_tab, pred_tab, llm_tab = st.tabs(["📊 Data Visualization", "🔮 Predictive Models", "🤖 LLM Use Cases"])
        for tab in [viz_tab, pred_tab, llm_tab]:
            with tab:
                st.info("Healthcare analytics projects coming soon!")

    with other_tab:
        viz_tab, pred_tab, llm_tab = st.tabs(["📊 Data Visualization", "🔮 Predictive Models", "🤖 LLM Use Cases"])
        for tab in [viz_tab, pred_tab, llm_tab]:
            with tab:
                st.info("More projects coming soon!")