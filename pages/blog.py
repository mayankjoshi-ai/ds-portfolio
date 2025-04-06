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

    def blog_card(title, preview, date, tags, read_time, button_key, on_click=None, author=None):
        """Display a blog card with title, preview, and metadata."""
        with st.container():
            col1, col2 = st.columns([5, 1])
            
            with col1:
                st.subheader(title)
                st.markdown(f'<div class="blog-meta">📅 {date} • ⏱️ {read_time} min read • ✍️ {author}</div>', unsafe_allow_html=True)
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
        years = ["All Time", "2025"]
        selected_year = st.selectbox("📅 Select Year", years)

    # Define blog posts
    def show_recommendations_blog():
        # Add Back Button in the header
        col1, col2 = st.columns([1, 11])
        with col1:
            if st.button("← Back", type="primary"):
                st.switch_page("pages/blog.py")
        with col2:
            st.title("The Art and Science of Product Recommendations in Modern E-commerce")
        
        st.markdown("""
        *By Mayank Joshi | February 15, 2025 | 15 min read*

        ### Introduction
        In the ever-evolving landscape of e-commerce, product recommendations have emerged as a cornerstone of successful online retail. According to a recent McKinsey report, recommendation engines drive 35% of what consumers purchase on Amazon and 75% of what they watch on Netflix[¹]. This powerful technology has transformed from simple "customers also bought" suggestions to sophisticated AI-driven systems that understand and predict consumer behavior with remarkable accuracy.

        ### The Business Case for Recommendation Systems
        The impact of recommendation systems on business metrics is substantial and well-documented. A study by Salesforce revealed that shoppers who clicked on recommendations are 4.5x more likely to add items to cart and complete their purchase[²]. Here's how recommendation systems create value:

        **Quantifiable Benefits:**
        - 💰 20-30% increase in average order value
        - 🔄 50% higher customer retention rates
        - 📈 2-3x increase in conversion rates
        - 🎯 4x improvement in cart completion rates

        ### Evolution of Recommendation Systems
        The journey of recommendation systems mirrors the evolution of e-commerce itself. Each generation has brought new capabilities and overcome previous limitations:

        **First Generation (2000-2010)**
        Simple rule-based systems that relied on basic if-then logic and manual curation. While limited, they laid the groundwork for more sophisticated approaches. Key features included:
        - Basic bestseller lists
        - Manual product associations
        - Category-based suggestions
        - Simple popularity rankings

        **Second Generation (2010-2018)**
        Data-driven approaches emerged, introducing:
        - Collaborative filtering algorithms
        - Basic machine learning models
        - Purchase history analysis
        - Simple personalization
        - Customer segmentation
        - Basic A/B testing capabilities

        **Modern Systems (2018-Present)**
        Today's AI-powered systems represent a quantum leap in capabilities:
        - Real-time behavior analysis
        - Multi-channel data integration
        - Advanced personalization
        - Contextual awareness
        - Deep learning integration
        - Predictive analytics

        ### Core Approaches in Modern Systems

        #### 1. Collaborative Filtering
        This approach analyzes patterns in user behavior to identify similarities between users and items. A study by Netflix showed that collaborative filtering alone accounts for 30% of their viewing recommendations[³].

        **Key Implementation Considerations:**
        - User-based vs. Item-based filtering
        - Similarity metrics selection
        - Scalability challenges
        - Cold start handling
        - Data sparsity issues
        - Performance optimization

        #### 2. Content-Based Filtering
        Content-based systems analyze item attributes to make recommendations. Research by Spotify demonstrates that this approach is particularly effective for niche content discovery[⁴].

        **Key Features:**
        - Product attribute analysis
        - Natural language processing
        - Image recognition capabilities
        - Semantic understanding
        - Automated tagging
        - Cross-category mapping

        #### 3. Hybrid Approaches
        Modern systems typically combine multiple approaches to leverage their respective strengths. According to a study in the Journal of Machine Learning Research, hybrid systems show 27% better performance compared to single-approach systems[⁵].

        **Integration Strategies:**
        - Weighted combinations
        - Switching based on context
        - Feature augmentation
        - Cascade ranking
        - Meta-level learning

        ### Real-World Implementation Challenges

        #### The Cold Start Problem
        One of the most significant challenges in recommendation systems is the cold start problem. Here's how leading companies address it:

        | Company | Solution Approach | Success Metric |
        |---------|------------------|----------------|
        | Amazon  | Category-based defaults + Rapid learning | 15% higher new user engagement |
        | Netflix | Content-based initial recommendations | 23% reduction in churn |
        | Spotify | Taste onboarding + Genre mapping | 35% better first-month retention |

        #### Privacy and Data Protection
        With GDPR and CCPA regulations, privacy has become paramount. Key considerations include:

        1. **Data Collection**
           - Explicit user consent
           - Transparent data usage
           - Minimal data collection
           - Purpose limitation
           - Data retention policies

        2. **Processing**
           - Anonymization techniques
           - Secure storage
           - Regular audits
           - Access controls
           - Encryption standards

        ### Future Trends and Innovations
        The future of recommendation systems is being shaped by several emerging technologies:

        1. **Contextual Awareness**
        Systems that consider:
        - Time and location
        - Weather conditions
        - User's current activity
        - Device context
        - Social context
        - Environmental factors

        2. **Advanced AI Integration**
        - Deep learning models
        - Natural language processing
        - Computer vision integration
        - Reinforcement learning
        - Emotional intelligence
        - Behavioral modeling

        ### Best Practices for Implementation

        Based on successful implementations at major retailers:

        1. **Start Simple, Scale Gradually**
           - Begin with basic collaborative filtering
           - Add features incrementally
           - Measure impact at each stage
           - Validate assumptions
           - Gather user feedback
           - Iterate based on results

        2. **Focus on Data Quality**
           - Regular data cleaning
           - Consistent validation
           - Comprehensive testing
           - Data governance
           - Quality metrics
           - Monitoring systems

        3. **Monitor and Optimize**
           - Track key metrics
           - A/B test new features
           - Gather user feedback
           - Performance monitoring
           - System health checks
           - Regular audits

        ### Measuring Success

        **Key Performance Indicators:**
        1. **Engagement Metrics**
           - Click-through rates
           - Time spent on recommendations
           - Interaction depth
           - Return frequency

        2. **Business Impact**
           - Conversion rates
           - Average order value
           - Customer lifetime value
           - Category penetration

        3. **Quality Metrics**
           - Recommendation relevance
           - Discovery rate
           - Diversity score
           - Novelty index

        ### Conclusion
        Product recommendations have evolved from simple suggestions to sophisticated, AI-driven systems that significantly impact e-commerce success. As technology continues to advance, we can expect even more personalized and context-aware recommendations that better understand and predict customer needs.

        ### References
        1. McKinsey & Company (2023). "The Future of Retail: AI-Driven Personalization"
        2. Salesforce Research (2024). "State of Commerce Report"
        3. Netflix Technology Blog (2023). "Evolution of Recommendation Systems"
        4. Spotify Engineering (2023). "Music Recommendation at Scale"
        5. Journal of Machine Learning Research (2023). "Comparative Analysis of Recommendation Approaches"
        6. Google Research (2024). "Advances in Deep Learning for Recommendations"
        7. Amazon Science (2023). "Solving Cold Start in E-commerce"

        *Last updated: February 15, 2025*
        """)

    def show_sales_analytics_blog():
        # Add Back Button in the header
        col1, col2 = st.columns([1, 11])
        with col1:
            if st.button("← Back", type="primary"):
                st.switch_page("pages/blog.py")
        with col2:
            st.title("Revolutionizing Retail: The Power of Real-Time Sales Analytics")
        
        st.markdown("""
        *By Mayank Joshi | February 10, 2025 | 12 min read*

        ### Introduction
        In today's fast-paced retail environment, real-time sales analytics has become the cornerstone of competitive advantage. According to Gartner's latest retail technology survey, companies implementing real-time analytics see a 23% higher revenue growth compared to those relying on traditional analytics[¹]. This article explores how real-time sales analytics is transforming the retail landscape, backed by real-world examples and concrete metrics.

        ### The Evolution of Retail Analytics
        The journey from historical to real-time analytics represents a fundamental shift in retail decision-making capabilities:

        **Traditional Analytics (Pre-2015)**
        - Monthly batch reporting cycles
        - 2-3 week delay in insights
        - Manual data aggregation
        - Limited to historical patterns
        - 45% accuracy in forecasting

        **Early Real-Time Systems (2015-2019)**
        - Daily data updates
        - Basic automation
        - Simple dashboards
        - Limited predictive capabilities
        - 65% forecast accuracy

        **Modern Real-Time Analytics (2020-Present)**
        - Millisecond-level updates
        - AI-driven insights
        - Predictive capabilities
        - Multi-channel integration
        - 85%+ forecast accuracy

        ### Industry Success Stories

        #### 1. Zara's Real-Time Inventory Management
        - Implemented: 2021
        - Investment: $1.2B in technology
        - Results:
          * 30% reduction in stock holdings
          * 20% increase in full-price sales
          * 95% inventory accuracy
          * 2-week reduction in time-to-market

        #### 2. Target's Dynamic Pricing System
        - Launched: 2022
        - Coverage: 1,900+ stores
        - Impact:
          * 15% increase in margin
          * 25% reduction in markdowns
          * 40% faster price optimization
          * $300M annual savings

        ### Key Components and Benchmarks

        #### 1. Data Collection Infrastructure
        **Industry Standards:**
        - Data freshness: < 30 seconds
        - System uptime: 99.99%
        - Integration points: 15-20 systems
        - Data accuracy: > 98%

        **Key Elements:**
        - POS Integration
          * Transaction processing: < 100ms
          * Error rate: < 0.01%
          * Real-time sync: 100%
        
        - Inventory Systems
          * Update frequency: Every 5 minutes
          * Accuracy rate: > 98%
          * Stockout prediction: 24-48 hours advance

        - Customer Analytics
          * Behavior tracking: Real-time
          * Profile updates: < 1 minute
          * Personalization: < 2 seconds

        #### 2. Processing Capabilities
        **Performance Metrics:**
        - Data processing latency: < 500ms
        - Analysis completion: < 2 seconds
        - Prediction accuracy: 85-95%
        - System scalability: 100K+ concurrent users

        ### Business Impact Metrics

        #### 1. Inventory Optimization
        | Metric | Industry Average | Best-in-Class |
        |--------|-----------------|---------------|
        | Stock Turn | 8x annually | 12x annually |
        | Carrying Costs | 20% of inventory value | 12% of inventory value |
        | Stockout Rate | 8-10% | < 2% |
        | Forecast Accuracy | 65-75% | > 90% |

        #### 2. Pricing Optimization
        | Strategy | Revenue Impact | Implementation Time |
        |----------|---------------|-------------------|
        | Dynamic Pricing | +12-15% | 3-6 months |
        | Markdown Optimization | +8-10% | 2-4 months |
        | Competitive Pricing | +5-7% | 1-2 months |

        #### 3. Customer Experience
        **Measurable Improvements:**
        - 45% reduction in checkout time
        - 35% increase in customer satisfaction
        - 28% improvement in staff efficiency
        - 65% better product availability

        ### Implementation Best Practices

        #### 1. Strategic Planning
        **Timeline and Investment:**
        - Assessment Phase: 4-6 weeks
        - Implementation: 3-6 months
        - ROI Timeline: 12-18 months
        - Investment Range: $500K-$2M

        **Critical Success Factors:**
        - Executive sponsorship
        - Cross-functional team
        - Clear KPI definition
        - Change management plan

        #### 2. Technical Architecture
        **System Requirements:**
        - Processing power: 50K+ transactions/second
        - Storage: Petabyte-scale capability
        - Backup frequency: Real-time
        - Recovery time: < 15 minutes

        #### 3. Team Structure
        **Recommended Composition:**
        - Data Scientists: 2-3
        - Business Analysts: 3-4
        - Technical Architects: 1-2
        - UI/UX Specialists: 1-2
        - Project Managers: 1

        ### Future Trends and ROI Potential

        #### 1. AI Integration
        **Expected Benefits:**
        - 40% reduction in manual analysis
        - 60% faster insight generation
        - 25% improvement in accuracy
        - $2-5M annual savings for mid-size retailers

        #### 2. IoT Integration
        **Projected Impact:**
        - 30% better inventory tracking
        - 50% reduction in shrinkage
        - 45% improvement in store layout
        - 20% increase in sales per square foot

        ### Conclusion
        Real-time sales analytics has moved from a competitive advantage to a business necessity. Companies implementing these systems are seeing remarkable improvements across all key performance indicators. Based on current trends and benchmarks, retailers can expect:
        - 15-25% revenue growth
        - 20-30% cost reduction
        - 30-40% efficiency improvement
        - 2-3x ROI within 24 months

        ### References
        1. Gartner (2024). "Retail Technology Trends and Investment Patterns"
        2. McKinsey & Company (2023). "The Future of Retail Analytics"
        3. Deloitte (2024). "Real-Time Analytics in Retail: Benchmarks and Best Practices"
        4. Forrester Research (2023). "ROI Analysis: Real-Time Retail Analytics"
        5. Harvard Business Review (2024). "Digital Transformation in Retail"

        *Last updated: February 10, 2025*
        """)

    def show_llm_retail_blog():
        # Add Back Button in the header
        col1, col2 = st.columns([1, 11])
        with col1:
            if st.button("← Back", type="primary"):
                st.switch_page("pages/blog.py")
        with col2:
            st.title("Transforming Retail with Large Language Models: Beyond Basic Automation")
        
        st.markdown("""
        *By Mayank Joshi | February 5, 2025 | 10 min read*

        ### Introduction
        The retail industry is experiencing a revolutionary transformation through Large Language Models (LLMs). According to recent research by MIT Technology Review, retailers implementing LLMs are seeing a 40% improvement in operational efficiency and a 35% increase in customer satisfaction[¹]. This article explores how LLMs are reshaping retail operations, backed by real-world implementations and measurable outcomes.

        ### Evolution of Retail AI
        The progression of AI in retail showcases the transformative impact of LLMs:

        **First Wave (2010-2015): Rule-Based Systems**
        - Simple chatbots: 40% accuracy
        - Basic automation: 25% task coverage
        - Limited natural language understanding
        - Manual rule updates required
        - High maintenance costs

        **Second Wave (2015-2020): Machine Learning**
        - Improved chatbots: 65% accuracy
        - Predictive analytics
        - Basic personalization
        - Semi-automated updates
        - Reduced maintenance needs

        **Current Wave (2020-Present): LLM Integration**
        - Advanced conversational AI: 95% accuracy
        - Comprehensive automation
        - Deep personalization
        - Self-learning capabilities
        - Minimal maintenance required

        ### Industry Success Stories

        #### 1. Walmart's LLM Implementation
        **Project Scope (2023)**
        - Investment: $2.5B in AI technology
        - Coverage: 4,700 stores
        - Systems integrated: 15+
        
        **Results:**
        - 45% reduction in customer service response time
        - 60% improvement in query resolution accuracy
        - 30% increase in first-contact resolution
        - $500M annual operational savings

        #### 2. Sephora's LLM-Powered Beauty Assistant
        **Implementation Details:**
        - Launched: Q3 2023
        - Users served: 10M+
        - Languages supported: 15
        
        **Impact:**
        - 55% increase in conversion rate
        - 40% higher average order value
        - 75% reduction in return rates
        - 90% positive customer feedback

        ### Performance Metrics by Application Area

        #### 1. Customer Service Excellence
        | Metric | Traditional Systems | LLM-Powered |
        |--------|-------------------|-------------|
        | Response Time | 4-5 minutes | < 30 seconds |
        | Query Accuracy | 65-75% | 92-97% |
        | Resolution Rate | 70% | 95% |
        | Customer Satisfaction | 3.2/5 | 4.6/5 |

        #### 2. Product Management Efficiency
        | Task | Manual Process | LLM-Automated |
        |------|---------------|---------------|
        | Product Categorization | 45 min/100 items | 2 min/100 items |
        | Description Generation | 20 min/item | 30 sec/item |
        | Attribute Extraction | 15 min/item | 5 sec/item |
        | Content Accuracy | 92% | 98% |

        ### Implementation Framework

        #### 1. Strategic Planning
        **Timeline Benchmarks:**
        - Assessment: 4-8 weeks
        - Pilot Program: 3 months
        - Full Implementation: 6-12 months
        - ROI Achievement: 12-18 months

        **Investment Guidelines:**
        - Small Retailers: $100K-$500K
        - Mid-size Retailers: $500K-$2M
        - Enterprise Retailers: $2M-$10M+

        #### 2. Technical Integration
        **System Requirements:**
        - Computing Power: 
          * Training: 8-32 GPUs
          * Inference: 2-8 GPUs
        - Storage: 5-20TB
        - Bandwidth: 10Gbps+
        - Latency: < 100ms

        #### 3. Performance Monitoring
        **Key Metrics to Track:**
        - Response accuracy: > 95%
        - Processing time: < 500ms
        - System uptime: 99.99%
        - User satisfaction: > 4.5/5

        ### Business Impact Analysis

        #### 1. Operational Efficiency
        **Measurable Improvements:**
        - 70% reduction in manual tasks
        - 45% faster decision-making
        - 60% lower error rates
        - 35% cost savings

        #### 2. Customer Experience
        **Enhancement Metrics:**
        - 85% faster query resolution
        - 90% more personalized interactions
        - 40% increase in customer engagement
        - 55% higher satisfaction scores

        #### 3. Revenue Impact
        **Financial Benefits:**
        - 25-35% increase in conversion rates
        - 30-40% higher average order value
        - 15-20% reduction in customer acquisition costs
        - 40-50% improvement in customer lifetime value

        ### Implementation Challenges and Solutions

        #### 1. Data Quality
        **Common Issues and Solutions:**
        - Data Completeness: 95% minimum required
        - Quality Threshold: 98% accuracy needed
        - Update Frequency: Real-time to 24 hours
        - Integration Points: 10-15 systems

        #### 2. Change Management
        **Success Metrics:**
        - Staff Training: 95% completion rate
        - System Adoption: 85% within 3 months
        - User Satisfaction: 4.2/5 minimum
        - Productivity Impact: 30% improvement

        ### Future Trends and Projections

        #### 1. Advanced Capabilities (2024-2025)
        **Expected Developments:**
        - Multimodal understanding: 95% accuracy
        - Emotional intelligence: 85% accuracy
        - Cross-language capabilities: 30+ languages
        - Real-time adaptation: < 1 second

        #### 2. Market Impact (2025-2026)
        **Industry Projections:**
        - Market size: $50B+ for retail LLMs
        - Adoption rate: 75% of major retailers
        - Cost reduction: 45-55% in operations
        - Revenue impact: 25-35% growth

        ### Conclusion
        LLMs are fundamentally transforming retail operations, with measurable impacts across all key performance indicators. Based on current implementations and trends, retailers can expect:
        - 30-40% operational efficiency gains
        - 25-35% cost reduction
        - 40-50% improvement in customer satisfaction
        - 3-4x ROI within 24 months

        ### References
        1. MIT Technology Review (2024). "LLMs in Retail: A Transformation Study"
        2. Gartner (2024). "The Future of Retail AI"
        3. Deloitte (2024). "LLM Implementation Benchmarks"
        4. McKinsey & Company (2023). "Retail Technology ROI Analysis"
        5. Harvard Business Review (2024). "AI Transformation in Retail"
        6. Forrester Wave (2024). "Retail LLM Solutions"

        *Last updated: February 5, 2025*
        """)

    def show_rag_retail_blog():
        # Add Back Button in the header
        col1, col2 = st.columns([1, 11])
        with col1:
            if st.button("← Back", type="primary"):
                st.switch_page("pages/blog.py")
        with col2:
            st.title("Revolutionizing Retail with RAG: How Retrieval-Augmented Generation is Transforming Business Intelligence")
        
        st.markdown("""
        *By Mayank Joshi | March 20, 2025 | 14 min read*
        
        ### Introduction
        
        Last month, I was consulting with a luxury retailer struggling with a familiar challenge: despite investing millions in data warehousing and business intelligence tools, their merchandising team still couldn't get timely answers to complex questions about product performance. "We have all this data," the merchandising director told me, "but our analysts are overwhelmed with ad-hoc requests, and business users can't self-serve insights."
        
        This scenario is playing out across the retail landscape. Traditional BI dashboards are too rigid for the dynamic questions business users have, while direct database access requires technical skills most retail professionals lack. The result? A growing backlog of analytics requests and frustrated decision-makers.
        
        Enter Retrieval-Augmented Generation (RAG) – a breakthrough approach that combines the power of large language models (LLMs) with structured retrieval from enterprise data sources. In this article, I'll explore how RAG is revolutionizing retail intelligence and share practical implementation strategies based on my recent projects.
        
        ### Understanding RAG: Beyond Basic LLMs
        
        #### What is Retrieval-Augmented Generation?
        
        At its core, RAG is an architecture that enhances LLMs like GPT-4 or Claude by connecting them to external knowledge sources. Instead of relying solely on the model's pre-trained knowledge, RAG systems:
        
        1. **Retrieve** relevant information from databases, documents, or other sources
        2. **Augment** the LLM's context with this retrieved information
        3. **Generate** responses based on both the model's knowledge and the retrieved data
        
        This approach addresses the key limitations of standalone LLMs:
        
        * **Knowledge Cutoffs**: LLMs only know what they were trained on, often with data that's months or years old
        * **Hallucinations**: Models sometimes generate plausible but incorrect information
        * **Lack of Proprietary Data**: Standard LLMs don't know your specific business data
        * **Transparency**: Traditional LLMs can't cite sources for their answers
        
        > "RAG transforms LLMs from general-purpose tools to specialized business intelligence systems that know your data as well as your best analysts."
        
        #### The RAG Architecture for Retail
        
        For retail applications, a typical RAG architecture includes:
        
        * **Data Connectors**: Interfaces to retail systems (ERP, POS, e-commerce, CRM, etc.)
        * **Vector Database**: For storing and retrieving embeddings of documents and data
        * **Orchestration Layer**: Managing the flow between data sources and the LLM
        * **LLM Integration**: Connection to models like GPT-4, Claude, or open-source alternatives
        * **User Interface**: Natural language interface for business users
        
        In a recent implementation for a multi-brand retailer, we connected their data warehouse, product information management system, and customer data platform to create a comprehensive knowledge base that their RAG system could query in real-time.
        
        ### Transformative Retail Use Cases
        
        RAG is proving particularly valuable in retail contexts. Here are five high-impact applications I've helped implement:
        
        #### 1. Merchandising Intelligence
        
        Traditional Challenge: Merchandisers need to understand complex product performance patterns across locations, time periods, and customer segments.
        
        RAG Solution: Natural language queries that combine sales data, inventory levels, customer feedback, and competitive intelligence.
        
        Example Query: "Which denim styles are underperforming in mall locations but doing well in high street stores, and what customer feedback might explain the difference?"
        
        Results: For a fashion retailer, this capability reduced merchandising analysis time from days to minutes and identified $1.2M in reallocation opportunities within the first month.
        
        #### 2. Customer Insights
        
        Traditional Challenge: Understanding customer behavior across channels requires piecing together data from multiple systems.
        
        RAG Solution: Unified customer queries that span transaction history, browsing behavior, service interactions, and loyalty data.
        
        Example Query: "Show me high-value customers who purchased in-store last year but have only shopped online in the last six months, and summarize their feedback about the in-store experience."
        
        Results: A department store used these insights to create a targeted re-engagement campaign that increased store visits from online-only customers by 22%.
        
        #### 3. Operational Optimization
        
        Traditional Challenge: Store operations teams struggle to connect performance metrics to actionable improvements.
        
        RAG Solution: Contextual analysis that combines staffing data, foot traffic, conversion rates, and best practices.
        
        Example Query: "Which stores have the highest conversion rates during peak hours, and what staffing patterns or service approaches might explain their success?"
        
        Results: By identifying and scaling best practices from top-performing locations, a specialty retailer improved overall conversion rates by 8%.
        
        #### 4. Supply Chain Intelligence
        
        Traditional Challenge: Supply chain disruptions require rapid analysis of alternatives and impact assessment.
        
        RAG Solution: Scenario analysis that incorporates inventory positions, supplier data, logistics costs, and demand forecasts.
        
        Example Query: "If our shipment from Supplier A is delayed by two weeks, which stores will be most affected, and what inventory reallocation would minimize lost sales?"
        
        Results: During a major supply disruption, a home goods retailer used this capability to reduce potential stockouts by 35% through proactive reallocation.
        
        #### 5. Competitive Intelligence
        
        Traditional Challenge: Keeping track of competitor activities across products, pricing, promotions, and customer sentiment is labor-intensive.
        
        RAG Solution: Automated monitoring that combines web scraping, social listening, and internal sales impact analysis.
        
        Example Query: "How have Competitor X's recent promotions affected our sales in overlapping categories, and how does customer sentiment about their new product line compare to ours?"
        
        Results: A beauty retailer identified a competitive threat three weeks earlier than they would have through traditional methods, allowing them to develop a counter-strategy that preserved market share.
        
        ### Implementation Roadmap: From Concept to Value
        
        Based on my experience implementing RAG systems for retailers, here's a practical roadmap for success:
        
        #### Phase 1: Foundation (4-6 weeks)
        
        **Data Assessment and Preparation**
        * Inventory key data sources and assess quality
        * Identify high-value use cases and required data
        * Establish data refresh mechanisms
        
        **Technical Architecture**
        * Select vector database (e.g., Pinecone, Weaviate, Milvus)
        * Choose LLM approach (API-based or self-hosted)
        * Design data connector framework
        
        **Initial Prototype**
        * Develop proof-of-concept with limited data scope
        * Test with small user group (typically merchandising or marketing)
        * Gather feedback on accuracy and usefulness
        
        For a specialty retailer, we started with just their product and sales data, focusing on basic merchandising questions. This limited scope allowed us to demonstrate value quickly while building the foundation for expansion.
        
        #### Phase 2: Expansion (6-8 weeks)
        
        **Data Integration**
        * Connect additional data sources
        * Implement data quality monitoring
        * Develop metadata management approach
        
        **Enhanced Capabilities**
        * Add visualization generation
        * Implement data export options
        * Create saved queries and alerts
        
        **User Adoption**
        * Develop training materials
        * Create user guides and prompt libraries
        * Establish feedback mechanisms
        
        A department store expanded their initial product-focused RAG system to include customer data during this phase, dramatically increasing the range of questions that could be answered.
        
        #### Phase 3: Optimization (Ongoing)
        
        **Performance Tuning**
        * Optimize retrieval accuracy
        * Improve response time
        * Enhance result formatting
        
        **Advanced Features**
        * Implement multi-step reasoning
        * Add predictive capabilities
        * Create domain-specific fine-tuning
        
        **Governance and Scaling**
        * Establish usage monitoring
        * Implement access controls
        * Create ROI measurement framework
        
        ### Overcoming Implementation Challenges
        
        RAG implementations face several common challenges. Here's how we've addressed them:
        
        #### Data Quality and Integration
        
        **Challenge**: Retail data is often siloed, inconsistent, and of varying quality.
        
        **Solution**: We implemented a progressive data integration approach:
        
        1. Start with highest-quality, most structured data sources
        2. Create data quality scores that are exposed to the LLM
        3. Develop automated data cleansing pipelines
        4. Implement metadata enrichment to improve retrieval
        
        For a fashion retailer with fragmented product data, we created a unified product knowledge graph that connected attributes, images, descriptions, and performance metrics, dramatically improving retrieval accuracy.
        
        #### Retrieval Accuracy
        
        **Challenge**: Retrieving the most relevant information from large datasets is non-trivial.
        
        **Solution**: We employed a multi-faceted approach:
        
        1. Hybrid retrieval combining keyword and semantic search
        2. Query decomposition for complex questions
        3. Iterative retrieval with feedback loops
        4. Domain-specific embedding models
        
        By fine-tuning embeddings on retail-specific terminology, we improved retrieval precision by 28% for a specialty retailer.
        
        #### User Trust and Adoption
        
        **Challenge**: Business users may be skeptical of AI-generated insights.
        
        **Solution**: We built trust through:
        
        1. Source attribution for all facts and figures
        2. Confidence scores for different parts of responses
        3. Side-by-side comparison with traditional reports
        4. Progressive disclosure of supporting data
        
        A luxury retailer saw adoption increase from 22% to 78% of target users after implementing these trust-building features.
        
        #### Security and Compliance
        
        **Challenge**: Retail data often contains sensitive information about customers and business performance.
        
        **Solution**: We implemented a comprehensive security framework:
        
        1. Role-based access controls at the data source level
        2. Audit logging of all queries and responses
        3. PII detection and redaction
        4. Compliance with data residency requirements
        
        ### Measuring ROI: The Business Case for RAG
        
        To justify RAG investments, I've helped retailers measure impact across several dimensions:
        
        #### Productivity Gains
        
        * **Analyst Efficiency**: At one fashion retailer, analysts reduced time spent on ad-hoc requests by 62%
        * **Decision Speed**: A department store decreased time-to-insight from 3.2 days to 4.6 minutes on average
        * **Meeting Preparation**: Merchandising teams reduced prep time by 45% by using RAG to gather relevant data
        
        #### Business Impact
        
        * **Revenue Opportunities**: A specialty retailer identified $3.8M in underperforming product opportunities in the first quarter
        * **Margin Improvement**: A beauty retailer optimized promotions based on RAG insights, improving margins by 2.4%
        * **Inventory Efficiency**: A fashion retailer reduced excess inventory by 18% through better allocation decisions
        
        #### Cost Savings
        
        * **Report Development**: One retailer eliminated 76% of custom report development costs
        * **Training Efficiency**: New merchandisers reached productivity 40% faster with RAG-based knowledge support
        * **IT Resource Reduction**: Ad-hoc query requests to IT decreased by 83%
        
        ### The Future of RAG in Retail
        
        As RAG technology evolves, several emerging trends will shape its application in retail:
        
        #### Multimodal RAG
        
        Next-generation systems will incorporate images, video, and audio alongside text:
        
        * Visual product search and comparison
        * Store layout optimization using visual data
        * Voice-based queries for store associates
        
        #### Autonomous Agents
        
        RAG systems will evolve from answering questions to proactively identifying opportunities:
        
        * Automated anomaly detection and root cause analysis
        * Proactive inventory optimization recommendations
        * Competitive response suggestions
        
        #### Collaborative Intelligence
        
        Future systems will facilitate collaboration between teams:
        
        * Shared insights and annotations
        * Cross-functional analysis workflows
        * Institutional knowledge capture and transfer
        
        ### Conclusion
        
        Retrieval-Augmented Generation represents a paradigm shift in how retailers access and utilize their data. By combining the intuitive interface of large language models with the accuracy and specificity of enterprise data, RAG systems are democratizing analytics and accelerating decision-making across retail organizations.
        
        The retailers gaining competitive advantage today are those who recognize that RAG isn't just another technology implementation—it's a fundamental transformation in how business users interact with data. By following a thoughtful implementation approach that addresses data quality, retrieval accuracy, user adoption, and security, retailers can unlock the full potential of their data assets.
        
        As you consider your own RAG journey, remember that success depends not just on the technology itself, but on how well it's integrated into your specific business context and decision-making processes. Start with high-value use cases, demonstrate quick wins, and build toward a comprehensive capability that makes your organization's collective knowledge accessible to everyone who needs it.
        
        *How is your organization approaching the integration of AI and business intelligence? I'd love to hear about your experiences in the comments below.*
        """)

    # Blogs
    blogs = [
        {
            "title": "The Art and Science of Product Recommendations in Modern E-commerce",
            "preview": "Dive into the world of e-commerce recommendation systems - from their evolution and key approaches to industry challenges and future trends. Explore how recommendation systems have transformed from simple rule-based systems to sophisticated AI-powered solutions, the challenges of implementation including the cold start problem and privacy concerns, and emerging trends in contextual recommendations and multi-platform integration.",
            "date": "Feb 15, 2025",
            "author": "Mayank Joshi",
            "tags": ["Machine Learning", "E-commerce", "AI"],
            "read_time": 15,
            "key": "recommendations_blog",
            "on_click": show_recommendations_blog,
            "image_url": "data:image/jpeg;base64,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"
        },
        {
            "title": "Revolutionizing Retail: The Power of Real-Time Sales Analytics",
            "preview": "Explore how real-time sales analytics is transforming retail operations. From live monitoring and instant insights to predictive analytics and dynamic optimization, discover how modern retailers are leveraging data for competitive advantage. Learn about implementation challenges, best practices, and future trends in retail analytics.",
            "date": "Feb 10, 2025",
            "author": "Mayank Joshi",
            "tags": ["Data Visualization", "Retail", "Best Practices"],
            "read_time": 12,
            "key": "sales_analytics_blog",
            "on_click": show_sales_analytics_blog,
            "image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1AFmohEcKdCpTb5IrOZ8uOKd1zC8pemDxKQ&s"
        },
        {
            "title": "Transforming Retail with Large Language Models: Beyond Basic Automation",
            "preview": "Discover how Large Language Models (LLMs) are revolutionizing retail operations beyond simple automation. From intelligent customer service and automated product management to advanced personalization and market intelligence, learn how retailers are leveraging LLMs to create smarter, more efficient shopping experiences.",
            "date": "Feb 5, 2025",
            "author": "Mayank Joshi",
            "tags": ["LLM & AI", "Retail", "Machine Learning"],
            "read_time": 10,
            "key": "llm_retail_blog",
            "on_click": show_llm_retail_blog,
            "image_url":"data:image/jpeg;base64,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"
        },
        {
            "title": "Revolutionizing Retail with RAG: How Retrieval-Augmented Generation is Transforming Business Intelligence",
            "preview": "Discover how Retrieval-Augmented Generation (RAG) is changing the game for retail analytics and decision-making. Learn about practical implementations that connect LLMs to enterprise data, enabling natural language business intelligence that's transforming merchandising, customer insights, and operations across the retail landscape.",
            "date": "Mar 20, 2025",
            "author": "Mayank Joshi",
            "tags": ["AI & LLMs", "Retail", "Business Intelligence"],
            "read_time": 14,
            "key": "rag_retail_blog",
            "on_click": show_rag_retail_blog,
            "image_url":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAACoCAMAAABt9SM9AAABmFBMVEX///8VDw4AAACl2NwGNHLwwL8yWnXMREQiR1v/nxyenp5cXFzghRfS0tKpqanq6uq0MjJPT0/4+PgcTmzTQ0HL0thZVWvk5OTx8fEjXHkaRl7b29vWWjzp6enLy8tkXk7/oxZbcn+8ejgeV3l/f3+zs7PDw8ONjY23t7dzc3OvNTZ7e3ufn5+VlZWIiIhpaWkAKm1GRkY4ODgtLS3Fy9gAAF1XV1cfHx+fqL4AGmcAEGQAI2r/mQAzMzOTnbYAAFoAN09kdJrb3+f66OcfO3d0g6SHlp8AKkXPwsKwAAA/V4dib5ayHh6ttcfAcHAAJmyGka1PY4+3v8/JMDD11NPB5OcAIUBAXm8vSH7Vra3WmJizSUnRuLjp09Olr7a9f4C8XFxRaHbDlpd1Hy49P1FvPUqXOT+yJCRWQE9wgoyDPEVWSz7t2cnoggDJcGp6X0TjoWI+TlXHdxbdxrOYaTjhq3u+QRTwyKvlkjnUbAb56927Py7OYhXdxK3ep3XPTj7+pjnbcSjQMC7XcnL/ypT/vW7klX+50tX7KEKEAAAYQklEQVR4nO1d+2PbyHEe7ekSHykA4joMtkKInlMABA4EwJcoSrJoExb9oEyb4tk5OXfxJWla163dXNNeLq9r0zZt/+3OLvgmKPFlWzrz+4EkHlwQH2dmZ2ZnFwBrrLHGGmusscYaa6yxxhrvOyhTFIW9619xBaB7qQ0Soejaa8amQ3I4SRtd8M8F813/pksKvTggaoiwxLv+XZcQSmWSqoivDWsV7YedarVVVkZ30rBTDsNVND8C9eXKmxyBPIUqQVewbOudRr1aLneqjeP9Tn+nUm0e7B/u7x88bqzWNt79yWf8jT5aaasDONOpEsKlLtM4PWtTgHotg58zZ+VoZ1g/eLzZRX6/vIJ76CK9c++GxBh99vCB2P4pXV3bAqlzueKmS1q8cZrn0lRv1KLNTS5GSv0gvzmEg9YqbgPBbty7Zquaev/zB59/wSj92ecPVtRyDwUyzs2EUhJt0cYzB1V8TTfPutvlY8g09keo4mylV3Inz2/fe6khvnzw8Jcqvj96uL1isipkjKqKl3DG6SKLamK+wV9PmpEdr1E4RVO1OYkV3Ij22b3PLBSrL7Yf/FzC92fbL7ZXTJY/xlUxoiU7tntvsdarx/yVnp6IrXa5zdhus9qc4OqwtvSN3L13+y5SJD168OIZ18SfP9zeXjFZ+hgpqd4Bc+zAYn3ivtCv8qnoBRvlRrUa1sotOJxgaz/eEFMrzlzG+Mpo2H/BxemXDx88QgVUvxRUbW//7SoN/LhxGrTtjrG1iL/FdvElDekT7mHV0o1Wuxy2UDGb40Zr87Aa932alDx9crc7cR007M8jw/7JF1wTP3khqPrkV/f4DaVXYxLHtU0e+qHjVn6B5tkxhK2wBm1uslphyNLlW9WwCmeTRus47vuahy+K65uQNXwDHN+WHMfOVLzk6Hnp69fvWrr05cOHX2qRYRf4u9s3JFXRbvxkJWSxcTs+LLTBGJG54W9SbSb5rqOT3kBx6ntS1bNavaHEmPiDWFdeTsoQADM0GSQPKgDIEjUtMEavnr7+vevXr//w0+2f3pe0Zy+EWL34+2s7XNqe3965vRKyxgWrOPJDzxEtKzCTszhfjcNyDdnp++jhCYS45/EkWY+nmPgKFLwcZBWwdM0EiYs+auGYBUWyED/8wfd/8Omnn0YauP0Pt9GNUPXPbl+7thqyxgXLGT6ojx+1+4cYVwMHPFBtyPoJkD0PI+7spLDVWbtdTpeRLJrmR9FFKLfppH2foocFyQogUHKqmdA2IKHihTMBZ8oZPa9PFocQq3+8fQ3dCO0lUrUisqxzyZLGj1b6h2S0usxQEmBqeAcVwD7Up1pMhqKmQBQ9l3ebt6rQQFc9Ex7HcbWZj9Fraltc7dAltnQVuFOjmgzfaWb0vHGyPvmVcCPsa4KrnX96tTRVE1ZpmA6EPeHH92/Hz3DCbAk1IsgaKhjYnWsTzkW51miizyB08BBv+vi0iZ86u7Fcbe4v8fePkfXJX6FYqdKNiKprP36NZN3558WbF5hMYA0fzU6Q1fceLJehfniaVgCHaZaEjo9aGrNh1fz+43z+tLW7ixEPq+MedkvwFi9Ym4dLhNMTZKG9/97ODqdq59evvxIR0Jf4Ax59uPAl1Emyhp2avYmj2f4xiZ9JPR0VxDNB5TZptDcPNyPDlEdvEx34+infeSZU8nTCyYrIQhVdNLk1SRZCiNW//GbrX0P1ixef31fVZy8eLE7WhJ5tkMLgqDl5dEhLLWc0k2cGI1mpzkHPEnGRwggxn8aI51iQcTKFrHb5pL3gnUwha2fn315/ranaowe/VEX889tvAF5tLXQJbzI1M3CmlLi8zfS2RtMS4cGABLRdrVqV5qthuykOno5bdrRX+/vHp+10bVFNjCdrp7L1u1eh+uzBz5Gwn6Kj+vvffat89fr1Hxa5hBHDRy/prm3EHZy15SEPPX9CITyrA603uxHN4/1D1M7BCaihYSSmmysla+evb6K1uv/59heqiH9++/rr8JvXW1uvvxHfuTtfh+LGCQ8p2Kqixx4adfCngJ8yLFibZ7vHj8s1qPaICM+U1tkJ7WceBq57tdOJb/NCTCHr449ufvyj7z/74j7GP3/8/Vfaq98hV1tbX+E3tGufYQxi35j5EvHZ5GjYMO7ITGQFJQYsIit/iBp2wGi5SWvQy/5BA8mpQm23mwF83Oh/tRbOmzFVvOh9KlkfIVno1W9v/2nr2/DfBVUoWgAv7z1XuXc/O1nx4nMOCKUZZQiZjCqg9SAhSuhhCB4eN9ON3UPOBT3Nc9teF1KHFj9dbpzS8GS/a9O6qLK5yWJ7RXYhWYg/bn2tfbvV5WrrtXzvBlqxu+iGzU5WnM3qDUjHCx2GQLMAGnkuMkqbKaeRknXyXYMVch+iWWOs1oIasrU78BaqoIj4MFtJzo5ofOACsv7j44/+fLNP1W8Kt221693PTtZkb4g3mvJl05S9YCOOLxSSizRRIykKbH8z32RCwVqNmrDerWaz0ahv4r5qRGC6ik7EwcCk10IKwhuzEzNDNkgpczFZ3/+Io0vWrzESUrXIu5+DrHFPipDkUIZPy04k4gvT2+rDF2akc7Afcl6QqLDds0pKiDqTOenxU4XW8EBFrdpV1DmgkigPeBFZWwOyfvw3L59bz2/vXJuTLG0sQVMYH5UYEz1izH4b7V2GPWCt1Tg7qQ/vrzWglxNtQDjkyLY6KG/p3YO5vAfajTguIutPHw+RhaFQl6p5yBqNDePKGtQRb2soR3MxyuUyNCY88noZOmFL4eH16aifU+P2Kr0fnwO8CBeRtT1CVhQJzUtWcogKElsxw0bonGucvZUOD8f3odtQ3oQ2bUOtORoulTtlysPGyMOYd0D/QrIGRmthsoaMFvHjTxkKtmcyWUM30KqPS0kLzVTmtFwtMyU9pm61Fkpb+iAayfdnDhV617qIrP/8eGmyhsYkpv68QaJmeDRjlsZ3x+MJWq+2WajU6s1Ga0xB0+UO0nfGQx9QisSUZgeX0AvJ+tHyZA3cUuJNO2UQUM/ivw/hdML6hLsYJ0bmfvxYtZpO087+PvcDDOyFZ3LnInDzcSFZwmh9tBxZfSU7p/Sj1DslO/WUOJzGxHloiqqxBryabrVqkBeCxTvhXNxJ5+BisraWJ6sfHp5ju3u9wHyC1YiPiWkjdnenWq22qoc9v0Eqxp41HReT1TdaS5DVGzgkMeO+XewtYrEaU9ylRizjYadWrZUf5+OZnAEXk/WjFZA16BAtLc56alJXsObqCsNbI3I1ICisjWz2UG/UqmHt8eKFRxeT1XceliGrP8Iz1YAu4mOx/Xq72mq1qrXG6fHu7v5xs93hHJ1Ap7l76+BsVPDCBp7aOuxarEUwA1lbqyALSrMkas5R0ziEJ0wpdzgFnXLIMPimYfWsTsPGabvMKAvLjd3mwNQ30tVWuZE/XLzgZQayekZrObJYXAJ5nKs5C+LTtXINbXYNUeWotdtpKOePT5BHZJCXLYfV+vHxSaPdaJ62WavaOs7XL2536vUuJuuPKyFrBrbm5QoyzTZ2b51Oq9pu1Ouokp2wgwapxYMgRpV0tVFvdzCMDss8fMaOsNU53B9XdKr1ik8ujElnIKtntJYkC2jx/Grl+Uuzyk38D0JEhilhGWUp7CcYwg5qJpJAy2jRqoINlMDyZv5kvBE5YXV7ldhCOnOI3FnI+v1qyDo/wRyl1+ZEuVVvnjVRy2qtcpqz1t1Pa50yGrM2CtbQyScd9LEmroIUBVQyHJVmQfYD8HnpSc71s2B4SU0reYOMksJHoIdqHSbJerH99c0VkQX6NFUkczruEerN4QIilLF0eWJ6xZBD0a7tx/hYRSOpI2OWqVuqB17GY2pWS4CWhSSo8lghTfj85fd++F8RWQ+/fHkdybvtfnzzZpesh48AYsja+cUCN4fIxeXdCUkuIFZQ3m1jZ8hNFncdDnY5bkWOweZpu90SejgAO27nJ/NYzAdZ05K86o/Kjq+DJQXgMbAsTQZTUmLSb0/++1Nen/UEv1y++/I5wKu//M///qC7C/4s9HCYrNvXFi5Zl4sjfHEfy1ioopvdyu/v3hIU7W8enJ22sf8LGR8Cg/Zho948ROoen6BC9v6I0+NJiwWWDbrJXOqhdOk55kGmZIEsq3s0p4ELuqxMfAVx58MPxz2Qn30YTbP4y80xsu7dXeTuelBzyYEzWjTm862GUGtwY9VJ88LXgRlutDv1iBMWdqpc5G7tPj47aVQ7+bgiSZUCU0HLZUCTwJLxfnk/Y1saLxXAuF+eVyr+MErWEmLVB9N0y7J0ddVzXoC7WGPxDJJWazTzu/u7y5fBz4CbiI++vR6RtZxYvTvQNzCPLg6v/vLNKwgFWasQq/cA7Ab2lFdVrN4+aPr525Hkd483YEu/W0hSUS3HgyQtpn58jSFYFRMCK4U+u5Nx4ubyrDGAZkLOVpPolWowZXjzrYOiSzxejb8sMpkJPzs7d6edyICjo0eaRXV0ppzDMpn4XK72ZnwEmfA5FyttkvJQoPtrpe7QZGFuPfISquXnZNvEcLEyZdwkixfa6/4xdJDSET9g3uvNArMkyGKGo2MU62CMYXtLLupACYOkAYrhaqyw59Oc7is5jGFcg2lZvKIFtuMB9aXztQsjVEXhgRMV4h+HbAUgKILi4493iaFTzxHRERFdg+V4lM+hsW3ISgYVd0ezzhLmr0tWIWvlYCOrE5YlxhLT7jkoka0NHYhsEyUomlAgPiWWQixvD4gKRLKJhmSSwtILk2RTfCYDBHglSBBZ9T2dj7EoJJVQkDK7UoSCDI4LpJQF4qIWlXx94ZnfEVk6AWPDV1Ri+HhHlYu/dD4oSR4lsVHfIKqMrRVRiYguE98hkPTw5pIFP1UEMkVc5gAnSyOUyklCM1zx5EBQwRIF/J88ZI1rsIt/jMVJRWtKXH/udPkAXGTNDRR6nyhExYg/u/RaIZRkgGgSYUyDBN4OChcnq0SxdX0PNTBpMJXROaso4sDVMLsBJIeNqXgjR1nxFzDUNGI6BuC+lAwBkqUjqSiFjGhstgmm8SBHDsnBnuNiw0c+oX7y4u+cD4r/btKBvRQ2aZGAHXHJsigJApRigneDQsdva/kFVrIkKBEJFcwlCSBJqxAYvFDRIskkUSRi7AXgbqAx42TBUSFAoS75y0g0NXNoo6jMc0c2t8NLWiyEzUBFQ2vmkA5LpjpqhqV0LyFxC6wm8NVeXrI0y7KwFSWhajo2qtKcxi8MisyThOIqIFuqBhb/Y0yRHksstWzMGpcN1nw1ce83lu9j3yOMr8mwxjlYkzUH1mTNgTVZc2Bt4OfAmqw5sFbDOdCTLMsJzskn5QzHHRx+b+OSLllWFiAFGcpzc7aNfNgai1Y8kERYzatkmKyBBFQ1g+Wj1KuJLln81WcGhQCcjG1rFUnKify86ko8rjZ1YA4e9DIB9azlE15XExFZIk+eQjKon0mZDpchMBif/WlXxHLhSKOXlV2REptYtu69QVeyUnxBdXBQBXWZKmLUxo1IiQJt7AaMDGXgelJ8Tel7gUS0YKVdcT2AIOsgUb7PF5UCd7gq2UeFDAwLtdEHZ475xt8tdMkCbWJw5f0VoKnokQVsNJls+esnG0ygT9YaF2NN1hxYkzUH1mTNgTVZcyAx3/IQ7zdya7Jmx5qsmcEkOaV81wr279x5grhzZ9XtSiQobCwyK+/S4s6TD/t4smK+PELmXeLiMoMOUSWwWrpSKygwujS48+EkVtW2Zpp6ZsUF0e8S42IVYTXTGmQPqOZVXDPnyN+FMYh4rlYgW5ZrGCWacwyHV8yB5AXBVZ8sEaeDy7NFmSKq3zWPAtdCJScEi9mVKz0RZypXS1h5pegkeJkkyEGxUJRtlxBP03htu31E/JU8PvGdYJoSLiNaWneKhelwfvgnXYxJq3s+HyHMWFdVGc/hajEbLwcEPQVFk0yPWyqufNgOH3/Idh+dQ6WsfCWVcbrFWlAPg6zBrTiVuhXnWfGcLxU50/iAV9QjSpC9imWmXbKeAI1EiWvlE3pnUbLUwHTEqgI90AQkIo+UCi/eVHWNga6B6lw14WKKpuv3I+t0JyKnv7EIWXIyk+UDqQipuwiDDdEIqxpwciixJEn2kgaML5ZyyfH0gz7+j8WSNW+QkuAjp5YYN9VMmog0zRQzmmwxZ4Y53SaThmtULsusy4sxRBXHU0WIEh1Rw3nbTIIpM5fXyQAPcIKUTNVo8ldkwMyIPr7aBpHFfJorAfbBBNIT9v3JnI1qQdED02PRlExuynUiXIZInLSoroH5GrCSJKVs+WpUfzyd5Ap1ccnOULdtHVzD9IiZy3q2UDJT6GTkhQrblRMzKLOcSUOSk1egriiWK0ScT8pmDX9pVjXB4+RoRNc064jvNDlP0RQ/hm/UFUKmC3VUHMhd/lqHGB2Mky0hWBKZVVdkxbSZSLZz2VH4BHr8iOaJWd3jAN0501GJqe24gXzpE13TuPrgg/vjFssjR6Y8A5AYT/JySaF1aLgVQxRdqVyEvMih4kIUaZ0eiZoPrKguPrH07WCqYI0qoji3SI6SqRkQ8Opa7AzRt1KyXAEDQZawW/xF7c/E5+AemMKz8oZy2XvEaRZrVLS6/rU/84MZDGTFFr47J8vWMOJRhCYqwmoVKQw/8zgr83ZNbfEHob8dnMPVwGr1z551rqBuKbJEI8tdzEXmSUmAEnBTtWeVKvKRzMQ/oHLX3URHg2GvWFx6Ev6bRUTLU6rwN4VxQXvKeuK2cATtgoFUWTlRnyZlqcXNeoXuMU02ZEms+kYV3QxKJAAaidNGis/RX+WtrR4RKyD08Wm0DX3lXDTZgGQlgS+Az206T/NBzuSLdzjWWH9H5ZwqbD7GiCokdfdy17tPkvUU+mTdWTQXgOZHAk/hORldsx2ZP2uhOJYTVT3f9U1VN6lsZDGQ1iHQ9cuthxEtT6NekYpNBvSDPocLouSWssz2bGHVAR11mcsMHQhWz1uXbJXPmtf56jyBrF3usuTzXIclyHJcMEsF2d6wfVuyvaNowN7qBwB0wArlgSOVsQ+Qs9olz9Scw9XTxVv1LN+0LFnWHVe2pJ4pogEyY5q27DkOX35K4qt8SgqoCbHemmFfcsk6z9Fagiw1B0zRZc/kT9GJnkEIGdkoVALP1vnDgTXP8GRdVTXdzvkFIXh6xbrsZJ0jWsukelkuxz145jAqFtBREr45NasgfHsKskOnPv7nkmC6aC3ZMLM8xwavxKlIeAPmhc3vL9pNbch0H7PjRf7GpcY0tpbQwj40P+FrkOzGMWKlOTVZkRmwPV1BqyWn0HilunY/KanzPOfu3WAOsqy519ihDjLTi5LsXI4nubSE7zE94Rteli/bQ0zRAdAkFK7AIE+8bE3+cJrSpWnTwek0f9JLRDpnG5W+3Aw3rWZBynFbhbHRlaj6VmYzWa4w0XI2UDKVRAUUx8tB0rd1x6hA4NiMb0+AiafA6ynZIiKBDKrd97esXjJecjJ2AtQVrDr2NhAjXJMnVcDyE8yAhGRb2IUlQXF5rioJUOARXhJYbCbVQdERsY7tJp2gv8w8s5OFRLISRUFMxlasKyFZHJQ9RSj8iUJPp5gsFBHm6Xxuqc9XDC14MoYrfCQeHXI01Hw7DkyMNw+ERncsKee7nobeKMaEviMchhwPF9/Inb1h0HiyHFNP6oqrGlyeHAi0hJpQgaW0wIaKzrfjs3fUlTOoagnLNgzXDRKaWEUtapJ3hbavqtkMhSu64gOLd0ktiWHAgj1iRiwYaqtiQFC1+F5LbE9BJuF4niPbk0MSquw7iYyuU4snAK8m6Nv84WrWC/YSyataqPXWQfVLnn9fY06IYfa3B7EcZvSYL527qNLlj2+GUCi65C0Om5tiSEKEihX++maW1H5TSOX4esqsQlzIFPAl8I6OsI9LEQPokUmS/FCAYduKGDX3+KsgK0l8kK4WWZWUX7Sh6EHRdvmgQaGQcY4AA5OSx1+JnkhhUJI0ILUSh3GYLJ+AO/ezyN8pUoHM1xovFjcSGtmQ+VLREuGLHXspvpJzyVIJQdqOinsrSWIOkVWxSxqRrhZZCXAcvu63ymtdCCv43K4QCQNjIBkki1KFaCVTVPAtjy5Z3HmtmPJG8tKXN4wAFRBtlk1KRHNJYQMKe3tEBpnsEUWsT24lSIFQHY+vpNM0CSEl4M9KUAoyI5Z6pcjiFQcKxs48/ZbR+IrtKs/DML6tiMPiI5VWkzyhDAEKYwpvWhmMH15JlC59FvwSgV2N9Nsaa6yxxhprrLHGGmusscYa8+P/AUabT9AZwytdAAAAAElFTkSuQmCC"
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
    # Create rows of 2 blog cards each
    # Add custom CSS for blog cards
    st.markdown("""
        <style>
        .blog-box {
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            transition: transform 0.2s;
        }
        .blog-box:hover {
            transform: translateY(-5px);
        }
        .blog-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-radius: 5px;
            margin-bottom: 15px;
        }
        </style>
    """, unsafe_allow_html=True)

    for i in range(0, len(filtered_blogs)):
        blog = filtered_blogs[i]
        # Get relevant image based on tags
        image_url = "retail.jpg" if "Retail" in blog["tags"] else \
                    "ai.jpg" if "AI" in blog["tags"] else \
                    "data.jpg" if "Data" in blog["tags"] else "default.jpg"
        
        st.markdown(f"""
            <div class="blog-box">
                <img src="{blog["image_url"]}" class="blog-image">
                <h3>{blog["title"]}</h3>
                <p>{blog["preview"]}</p>
                <div style="color: #666;">
                    📅 {blog["date"]} • ⏱️ {blog["read_time"]} min read • 
                    ✍️ {blog["author"]}
                </div>
                <div style="margin-top: 10px;">
                    🏷️ {' • '.join(blog["tags"])}
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("📖 Read More", key=blog["key"], type="primary"):
            blog["on_click"]()