def show_page():
    import streamlit as st
    import sys
    import os

    # CSS for blog cards
    st.markdown("""
        <style>
        .blog-card {
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            border: 1px solid rgba(49, 51, 63, 0.2);
            transition: transform 0.3s ease;
        }
        .blog-card:hover {
            transform: translateY(-5px);
        }
        .blog-meta {
            color: #666;
            font-size: 0.9em;
            margin-bottom: 1rem;
        }
        .blog-preview {
            color: #444;
            margin: 1rem 0;
        }
        .read-more {
            color: #0096FF;
            text-decoration: none;
            font-weight: 500;
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

    def blog_card(title, preview, date, tags, read_time, button_key, on_click=None):
        """Display a blog card with title, preview, and metadata."""
        with st.container():
            col1, col2 = st.columns([5, 1])
            
            with col1:
                st.subheader(title)
                st.markdown(f'<div class="blog-meta">📅 {date} • ⏱️ {read_time} min read</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="blog-preview">{preview}</div>', unsafe_allow_html=True)
                st.caption(f"🏷️ {' • '.join(tags)}")
            
            with col2:
                st.write("")  # Add spacing
                button_clicked = st.button("📖 Read More", key=button_key, type="primary", use_container_width=True)
            
            if button_clicked:
                if on_click:
                    on_click()
                else:
                    st.info("Blog post coming soon!")
            
            st.markdown("---")

    st.title("Technical Blog")

    # Sidebar filters
    with st.sidebar:
        st.header("🔍 Filter Posts")
        st.markdown("---")
        
        # Category filter
        categories = ["All Categories", "Machine Learning", "Data Visualization", "LLM & AI", "Best Practices"]
        selected_category = st.selectbox("📊 Select Category", categories)
        
        # Date filter
        years = ["All Time", "2024", "2023", "2022"]
        selected_year = st.selectbox("📅 Select Year", years)

    # Define blog posts
    def show_recommendations_blog():
        # Add Back Button
        col1, col2 = st.columns([1, 11])
        with col1:
            if st.button("← Back", type="primary"):
                st.switch_page("pages/blog.py")
        with col2:
            st.title("The Art and Science of Product Recommendations in Modern E-commerce")
        
        st.markdown("""
        ### Introduction
        Product recommendations have become the backbone of modern e-commerce, fundamentally changing how customers discover and purchase products. From Amazon's "Customers who bought this also bought" to Netflix's personalized movie suggestions, recommendation systems are everywhere. But what makes them tick, and why are they so crucial in today's digital marketplace?

        ### Why Product Recommendations Matter
        The impact of recommendation systems extends far beyond simple product suggestions:
        - **Customer Experience**: Personalized shopping experiences that feel tailored to individual preferences
        - **Discovery**: Helping customers find products they didn't know they wanted
        - **Business Growth**: Increased average order value and customer lifetime value
        - **Inventory Management**: Better stock planning based on predicted customer interests
        - **Customer Retention**: Enhanced engagement leading to repeat purchases

        ### The Evolution of Recommendation Systems
        1. **First Generation**: Simple rule-based systems
           - Basic "bestsellers" lists
           - Category-based recommendations
           - Manual curation

        2. **Second Generation**: Data-driven approaches
           - Purchase history analysis
           - Collaborative filtering
           - Basic personalization

        3. **Modern Systems**: AI-powered recommendations
           - Real-time behavior analysis
           - Multi-channel data integration
           - Contextual awareness
           - Deep learning models

        ### Key Approaches in Modern Recommendation Systems

        #### 1. Collaborative Filtering
        - Based on user similarity patterns
        - "People who liked X also liked Y"
        - Handles complex preferences
        - Challenges with cold start and data sparsity

        #### 2. Content-Based Filtering
        - Uses product attributes and descriptions
        - Matches user preferences with product features
        - Great for niche products
        - Limited by available product metadata

        #### 3. Hybrid Systems
        - Combines multiple approaches
        - Balances different recommendation strategies
        - Adapts to various scenarios
        - More robust and flexible

        ### Industry Challenges and Solutions

        #### 1. The Cold Start Problem
        - New users with no history
        - New products with no interactions
        - Solutions: Default recommendations, content-based approaches

        #### 2. Data Quality and Privacy
        - GDPR and privacy regulations
        - Data collection limitations
        - Balancing personalization with privacy

        #### 3. Scale and Performance
        - Real-time processing requirements
        - Large product catalogs
        - High concurrent users

        ### Future Trends

        1. **Contextual Recommendations**
           - Weather-based suggestions
           - Location-aware recommendations
           - Time-sensitive offers

        2. **Multi-Platform Integration**
           - Unified customer view across channels
           - Consistent recommendations across devices
           - Cross-platform behavior analysis

        3. **Advanced AI Applications**
           - Natural language processing for better understanding
           - Computer vision for visual recommendations
           - Reinforcement learning for adaptive systems

        ### Best Practices for Implementation

        1. **Start Simple**
           - Begin with basic collaborative filtering
           - Gradually add complexity
           - Test and measure impact

        2. **Focus on Data Quality**
           - Clean and structured data
           - Regular data validation
           - Comprehensive product attributes

        3. **Consider User Experience**
           - Clear recommendation labels
           - Explanation of suggestions
           - Easy feedback mechanisms

        ### Measuring Success

        Key metrics to track:
        - Click-through rates
        - Conversion rates
        - Average order value
        - Customer satisfaction
        - Discovery metrics
        - Long-term engagement

        ### Conclusion
        Product recommendations are no longer optional in e-commerce. They're a critical tool for business growth and customer satisfaction. As technology evolves, we'll see even more sophisticated and personalized recommendation systems that better understand and predict customer needs.
        """)

    blogs = [
        {
            "title": "The Art and Science of Product Recommendations in Modern E-commerce",
            "preview": "Dive into the world of e-commerce recommendation systems - from their evolution and key approaches to industry challenges and future trends. Explore how recommendation systems have transformed from simple rule-based systems to sophisticated AI-powered solutions, the challenges of implementation including the cold start problem and privacy concerns, and emerging trends in contextual recommendations and multi-platform integration.",
            "date": "Feb 15, 2024",
            "tags": ["Machine Learning", "E-commerce", "AI"],
            "read_time": 15,
            "key": "recommendations_blog",
            "on_click": show_recommendations_blog
        }
    ]

    # Filter blogs based on selection
    filtered_blogs = blogs
    if selected_category != "All Categories":
        filtered_blogs = [b for b in filtered_blogs if selected_category in b["tags"]]
    if selected_year != "All Time":
        filtered_blogs = [b for b in filtered_blogs if selected_year in b["date"]]

    # Display blog count
    st.caption(f"Showing {len(filtered_blogs)} of {len(blogs)} posts")
    
    # Display filtered blogs
    for blog in filtered_blogs:
        blog_card(
            title=blog["title"],
            preview=blog["preview"],
            date=blog["date"],
            tags=blog["tags"],
            read_time=blog["read_time"],
            button_key=blog["key"],
            on_click=blog["on_click"]
        )