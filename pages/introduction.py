def show_page():
    import streamlit as st
    import time

    # Add animated character CSS and HTML before the main title
    st.markdown("""
        <style>
            /* Theme variables */
            :root {
                --background-color: #FFFFFF;
                --text-color: #333333;
                --card-background: rgba(245, 245, 245, 0.4);
                --card-hover-background: rgba(245, 245, 245, 0.6);
                --timeline-color: #0096FF;
                --border-color: rgba(0, 0, 0, 0.1);
                --impact-background: rgba(245, 245, 245, 0.8);
                --download-gradient: linear-gradient(135deg, #f6f8f9 0%, #e5ebee 100%);
                --shine-gradient: rgba(0, 150, 255, 0.1);
            }

            /* Dark mode */
            @media (prefers-color-scheme: dark) {
                :root {
                    --background-color: #1E1E1E;
                    --text-color: #FFFFFF;
                    --card-background: rgba(45, 45, 45, 0.4);
                    --card-hover-background: rgba(55, 55, 55, 0.6);
                    --timeline-color: #00B4FF;
                    --border-color: rgba(255, 255, 255, 0.1);
                    --impact-background: rgba(45, 45, 45, 0.8);
                    --download-gradient: linear-gradient(135deg, #2d2d2d 0%, #1e1e1e 100%);
                    --shine-gradient: rgba(0, 180, 255, 0.1);
                }
            }

            /* Character container */
            .character-container {
                position: fixed;
                bottom: -100%;
                right: 20px;
                width: 150px;
                height: 200px;
                z-index: 1000;
                animation: slideUp 1s ease forwards 1s;
            }

            /* Speech bubble with fade out */
            .speech-bubble {
                position: absolute;
                background: var(--timeline-color);
                border-radius: 15px;
                padding: 15px;
                color: white;
                font-size: 16px;
                width: 150px;
                top: -80px;
                left: -80px;
                opacity: 0;
                animation: fadeInOut 5s ease forwards;
            }

            .speech-bubble:after {
                content: '';
                position: absolute;
                bottom: 0;
                right: 20%;
                width: 0;
                height: 0;
                border: 15px solid transparent;
                border-top-color: var(--timeline-color);
                border-bottom: 0;
                margin-bottom: -15px;
            }

            /* Animations */
            @keyframes slideUp {
                0% { bottom: -100%; }
                100% { bottom: 20px; }
            }

            @keyframes fadeInOut {
                0% { 
                    opacity: 0;
                    transform: translateY(20px);
                }
                10% {
                    opacity: 1;
                    transform: translateY(0);
                }
                80% {
                    opacity: 1;
                    transform: translateY(0);
                }
                100% {
                    opacity: 0;
                    transform: translateY(-20px);
                    visibility: hidden;
                }
            }

            @keyframes wave {
                0% { transform: rotate(0deg); }
                25% { transform: rotate(-20deg); }
                75% { transform: rotate(20deg); }
                100% { transform: rotate(0deg); }
            }

            /* Timeline card styles */
            .timeline-card {
                border-left: 2px solid var(--timeline-color);
                padding: 15px 20px;
                margin-bottom: 20px;
                position: relative;
                transition: all 0.3s ease;
                border-radius: 8px;
                background: var(--card-background);
                color: var(--text-color);
            }

            .timeline-card:hover {
                transform: translateX(10px);
                background: var(--card-hover-background);
                box-shadow: 0 4px 15px rgba(0, 150, 255, 0.2);
            }

            .timeline-card:before {
                content: '';
                width: 15px;
                height: 15px;
                background: var(--timeline-color);
                border-radius: 50%;
                position: absolute;
                left: -8.5px;
                top: 20px;
                transition: all 0.3s ease;
            }

            /* Impact metrics */
            .impact-metric {
                background-color: var(--impact-background);
                padding: 12px;
                border-radius: 8px;
                margin: 8px 0;
                border: 1px solid var(--border-color);
                transition: all 0.3s ease;
                cursor: pointer;
                color: var(--text-color);
            }

            .impact-metric:hover {
                transform: translateX(5px);
                border-color: var(--timeline-color);
                box-shadow: 0 4px 12px rgba(0, 150, 255, 0.2);
            }

            /* Download section */
            .download-section {
                background: var(--download-gradient);
                padding: 2rem;
                border-radius: 16px;
                margin: 2rem 0;
                text-align: center;
                position: relative;
                overflow: hidden;
                color: var(--text-color);
            }

            .download-heading {
                font-size: 1.8rem;
                color: var(--timeline-color);
                margin-bottom: 1rem;
                position: relative;
                display: inline-block;
            }

            .download-description {
                color: var(--text-color);
                font-size: 1rem;
                margin: 1rem 0;
                line-height: 1.5;
            }

            /* Expander styling */
            .stExpander {
                border: none !important;
                border-radius: 8px !important;
                background-color: var(--card-background) !important;
                color: var(--text-color) !important;
                transition: all 0.3s ease !important;
            }

            .stExpander:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 15px rgba(0, 150, 255, 0.15) !important;
            }
        </style>

        <div class="character-container">
            <div class="speech-bubble">
                Hey Yo! 👋<br>Dont forget to check out the Projects section, it has got crazy cool stuff! Thank me later😉
            </div>
            <svg class="character" viewBox="0 0 100 140">
                <!-- Body -->
                <circle cx="50" cy="50" r="30" fill="#2196F3"/>
                <!-- Head -->
                <circle cx="50" cy="30" r="20" fill="#FFB74D"/>
                <!-- Eyes -->
                <circle cx="43" cy="25" r="3" fill="#333"/>
                <circle cx="57" cy="25" r="3" fill="#333"/>
                <!-- Smile -->
                <path d="M40 35 Q50 45 60 35" stroke="#333" fill="none" stroke-width="2"/>
                <!-- Hand -->
                <circle cx="80" cy="50" r="8" fill="#FFB74D">
                    <animateTransform
                        attributeName="transform"
                        type="rotate"
                        from="0 80 45"
                        to="20 80 45"
                        dur="0.5s"
                        repeatCount="indefinite"
                        values="0 80 45; 20 80 45; 0 80 45"
                    />
                </circle>
            </svg>
        </div>
    """, unsafe_allow_html=True)
    
    st.title("🙋‍♂️ Welcome to Mayank's Data Science Portfolio!")
    # st.image("images/mayank_pic.jpg", caption="AI Scientist", use_container_width=True)
    st.write("Hi, I'm Mayank Joshi, a curious AI Scientist with 6+ years of experience in Data Science and Analytics who loves solving real-world problems with AI and analytics. From crafting predictive models to automating workflows, I bring ideas to life with data. Always innovating, always learning—I'm here to make technology work smarter, not harder, for everyone.")

    # Fun Fact Display
    st.info("""
    **Did You Know?**  
    Mayank means Moon 🌛 (No wonder I'm always over the moon about everything!! 🚀🤷🏻😂)
    """)

    # Career Timeline
    def create_professional_timeline():
        # Custom CSS for timeline styling
        st.markdown("""
                        <style>
                            /* Timeline card styles with hover effects */
                            .timeline-card {
                                border-left: 2px solid #0096FF;
                                padding-left: 20px;
                                margin-bottom: 20px;
                                position: relative;
                                transition: all 0.3s ease;
                                padding: 15px 20px;
                                border-radius: 8px;
                                background: rgba(245, 245, 245, 0.4);
                            }

                            .timeline-card:hover {
                                transform: translateX(10px);
                                background: rgba(245, 245, 245, 0.6);
                                box-shadow: 0 4px 15px rgba(0, 150, 255, 0.2);
                            }

                            .timeline-card:before {
                                content: '';
                                width: 15px;
                                height: 15px;
                                background: #0096FF;
                                border-radius: 50%;
                                position: absolute;
                                left: -8.5px;
                                top: 20px;
                                transition: all 0.3s ease;
                                box-shadow: 0 0 0 0 rgba(0, 150, 255, 0.7);
                            }

                            .timeline-card:hover:before {
                                background: #00B4FF;
                                box-shadow: 0 0 0 6px rgba(0, 150, 255, 0.2);
                                animation: pulse 1.5s infinite;
                            }

                            /* Pulse animation for timeline dots */
                            @keyframes pulse {
                                0% {
                                    box-shadow: 0 0 0 0 rgba(0, 150, 255, 0.7);
                                }
                                70% {
                                    box-shadow: 0 0 0 10px rgba(0, 150, 255, 0);
                                }
                                100% {
                                    box-shadow: 0 0 0 0 rgba(0, 150, 255, 0);
                                }
                            }

                            /* Impact metric styles with hover effects */
                            .impact-metric {
                                background-color: rgba(245, 245, 245, 0.8);
                                padding: 12px;
                                border-radius: 8px;
                                margin: 8px 0;
                                border: 1px solid rgba(0, 0, 0, 0.1);
                                transition: all 0.3s ease;
                                cursor: pointer;
                            }

                            .impact-metric:hover {
                                transform: translateX(5px);
                                background-color: rgba(245, 245, 245, 0.9);
                                border-color: rgba(0, 150, 255, 0.5);
                                box-shadow: 0 4px 12px rgba(0, 150, 255, 0.2);
                            }

                            /* Expander styles with hover effects */
                            .stExpander {
                                border: none !important;
                                border-radius: 8px !important;
                                background-color: #FFFFFF !important;
                                transition: all 0.3s ease !important;
                            }

                            .stExpander:hover {
                                transform: translateY(-2px);
                                box-shadow: 0 4px 15px rgba(0, 150, 255, 0.15) !important;
                            }

                            /* Company name styles */
                            .timeline-card h3 {
                                color: #0096FF !important;
                                transition: all 0.3s ease;
                            }

                            .timeline-card:hover h3 {
                                color: #00B4FF !important;
                            }

                            /* Role and period text styles */
                            .timeline-card p {
                                color: #333333 !important;
                                transition: all 0.3s ease;
                            }

                            .timeline-card:hover p {
                                color: #000000 !important;
                            }

                            /* Make expanders same height in a row */
                            [data-testid="stExpander"] {
                                height: 100%;
                            }
                        </style>
                    """, unsafe_allow_html=True)

        # Title
        st.title("Professional Timeline")

        # Experience Data
        experiences = [
            {
                "period": "Oct 2022 - Present",
                "company": "Apparel Group",
                "role": "Senior Data Scientist",
                "location": "Dubai, UAE",
                "projects": [
                    {
                        "name": "AI-Powered Auto-replenishment Engine",
                        "impacts": [
                            "🚀 Spearheaded implementation across 500+ stores in 30+ brands",
                            "📉 Optimized store replenishment cycles from 7 to 2 times weekly",
                            "📈 Boosted store product availability from 75% to 96%",
                            "💰 Drove AED 12M additional revenue through improved stock positioning",
                            "📊 Slashed stockout-related sales loss from 15% to 3%",
                            "⚡ Achieved 85% reduction in manual intervention, saving AED 800K annually"
                        ]
                    },
                    {
                        "name": "RITUALS ML Demand Forecasting Engine",
                        "impacts": [
                            "🎯 Enhanced forecast accuracy from 56% to 83% using XGBoost",
                            "⚡ Automated 95% of forecasting workflow (16 hours → 45 minutes)",
                            "💰 Reduced excess inventory by 22% through precise predictions",
                            "📊 Decreased safety stock requirements by 35% across warehouses"
                        ]
                    },
                    {
                        "name": "Supply Chain Analytics Platform",
                        "impacts": [
                            "🔄 Built end-to-end platform handling $500M annual inventory",
                            "📊 Integrated 15+ real-time KPIs tracking >2Million units annual replenishment",
                            "📈 Achieved 90% platform adoption across 30+ brands",
                            "⚡ Reduced reporting time by 75% through automation"
                        ]
                    }
                ]
            },
            {
                "period": "Feb 2022 - Oct 2022",
                "company": "Chalhoub Group",
                "role": "Data Scientist",
                "location": "Dubai, UAE",
                "projects": [
                    {
                        "name": "Real-time Inventory Intelligence Dashboard",
                        "impacts": [
                            "📊 Developed live tracking for $300M worth of luxury inventory",
                            "📈 Reduced dead stock by 25% through better visibility",
                            "💡 Enabled data-driven decisions for 200+ store managers"
                        ]
                    },
                    {
                        "name": "Smart Inter-store Transfer Engine",
                        "impacts": [
                            "⚡ Slashed transfer processing time from 8 hours to 20 minutes",
                            "💰 Generated 4.5% sales uplift ($2.8M annually)",
                            "🎯 Achieved 92% accuracy in transfer recommendations"
                        ]
                    }
                ]
            },
            {
                "period": "Feb 2021 - Feb 2022",
                "company": "Maytronics",
                "role": "Junior Data Scientist",
                "location": "Gurugram, Haryana",
                "projects": [
                    {
                        "name": "IoT-Based Water Quality Prediction System",
                        "impacts": [
                            "🤖 Built ML model achieving 91% accuracy in water quality prediction",
                            "📈 Reduced manual testing frequency by 60%",
                            "⚡ Enabled 24/7 automated monitoring for 1000+ pools",
                            "💰 Saved clients 40% in maintenance costs through predictive alerts"
                        ]
                    }
                ]
            },
            {
                "period": "Aug 2018 - Feb 2021",
                "company": "Colgate Palmolive",
                "role": "Data Analyst",
                "location": "Mumbai, India",
                "projects": [
                    {
                        "name": "AI Product Classification Engine",
                        "impacts": [
                            "⚡ Accelerated classification process by 93% (13 hours → 45 minutes) using MultiClass Classification Model",
                            "🎯 Achieved 88% accuracy in global product mapping",
                            "📊 Processed 50,000+ SKUs across 7 markets",
                        ]
                    },
                    {
                        "name": "Social Media Risk Analytics Platform",
                        "impacts": [
                            "🔍 Monitored 100K+ daily social media interactions from Twitter and Blogs",
                            "⚡ Achieved 92% accuracy in sentiment classification",
                            "📈 Reduced response time to negative mentions by 65%",
                            "🎯 Identified 15+ potential PR issues before escalation"
                        ]
                    }
                ]
            }
        ]

        # Display timeline
        for exp in experiences:
            with st.container():
                # Company header
                st.markdown(f"""
                    <div class="timeline-card">
                        <h3 style='margin:0;color:#0096FF;'>{exp['company']}</h3>
                        <p style='margin:0;color:#666;'>{exp['role']} | {exp['location']}</p>
                        <p style='margin:0;color:#888;font-size:0.9em;'>{exp['period']}</p>
                    </div>
                """, unsafe_allow_html=True)

                # Create columns for projects based on the number of projects
                num_projects = len(exp['projects'])
                cols = st.columns(num_projects)

                # Display projects in columns
                for idx, (project, col) in enumerate(zip(exp['projects'], cols)):
                    with col:
                        with st.expander(f"🚀 {project['name']}", expanded=False):
                            for impact in project['impacts']:
                                st.markdown(f"""
                                    <div class="impact-metric">
                                        {impact}
                                    </div>
                                """, unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)

    create_professional_timeline()

    # Specify a file from a folder
    st.markdown("""
            <style>
                /* Download section container */
                .download-section {
                    background: linear-gradient(135deg, #f6f8f9 0%, #e5ebee 100%);
                    padding: 2rem;
                    border-radius: 16px;
                    margin: 2rem 0;
                    text-align: center;
                    position: relative;
                    overflow: hidden;
                }

                /* Animated background effect */
                .download-section::before {
                    content: '';
                    position: absolute;
                    top: -50%;
                    left: -50%;
                    width: 200%;
                    height: 200%;
                    background: linear-gradient(
                        45deg,
                        transparent 0%,
                        rgba(0, 150, 255, 0.1) 50%,
                        transparent 100%
                    );
                    animation: shine 3s infinite;
                }

                @keyframes shine {
                    0% {
                        transform: translateX(-50%) translateY(-50%) rotate(0deg);
                    }
                    100% {
                        transform: translateX(-50%) translateY(-50%) rotate(360deg);
                    }
                }

                /* Download heading */
                .download-heading {
                    font-size: 1.8rem;
                    color: #1E88E5;
                    margin-bottom: 1rem;
                    position: relative;
                    display: inline-block;
                }

                /* Animated underline */
                .download-heading::after {
                    content: '';
                    position: absolute;
                    bottom: -5px;
                    left: 0;
                    width: 100%;
                    height: 3px;
                    background: #1E88E5;
                    transform: scaleX(0);
                    transform-origin: right;
                    transition: transform 0.5s ease;
                }

                .download-heading:hover::after {
                    transform: scaleX(1);
                    transform-origin: left;
                }

                /* Download button container */
                .download-button-container {
                    margin-top: 1rem;
                    position: relative;
                    display: inline-block;
                }

                /* Pulse animation for the download icon */
                @keyframes pulse-download {
                    0% {
                        transform: scale(1);
                    }
                    50% {
                        transform: scale(1.1);
                    }
                    100% {
                        transform: scale(1);
                    }
                }

                /* Download icon */
                .download-icon {
                    font-size: 2rem;
                    margin-bottom: 0.5rem;
                    animation: pulse-download 2s infinite;
                    display: inline-block;
                }

                /* Description text */
                .download-description {
                    color: #666;
                    font-size: 1rem;
                    margin: 1rem 0;
                    line-height: 1.5;
                }
            </style>
        """, unsafe_allow_html=True)

    # Create the download section with animations
    st.markdown("""
            <div class="download-section">
                <h2 class="download-heading">📄 Ready to Learn More?</h2>
                <p class="download-description">
                    Download my detailed resume to explore my complete professional journey, technical skills, and achievements.
                    <br>
                    <span style="font-size: 0.9em; color: #888;">
                        (PDF format • Last updated January 2024)
                    </span>
                </p>
                <div class="download-icon">⬇️</div>
            </div>
        """, unsafe_allow_html=True)

    # Add the actual download button with custom styling
    with open("resume/Resume.pdf", "rb") as resume_file:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.download_button(
                label="Download Full Resume",
                data=resume_file,
                file_name="Mayank_Joshi_Data_Scientist.pdf",
                mime="application/pdf",
                key="resume_download",
                help="Click to download my detailed resume in PDF format",
                use_container_width=True,
            )
