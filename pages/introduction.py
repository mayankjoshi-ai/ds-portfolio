def show_page():
    import streamlit as st
    import time

    st.title("🙋‍♂️ Welcome to Mayank's Data Science Portfolio!")
    # st.image("images/mayank_pic.jpg", caption="AI Scientist", use_container_width=True)
    st.write("Hi, I'm Mayank Joshi, a curious AI Scientist with 6+ years of experience in Data Science and Analytics who loves solving real-world problems with AI and analytics. From crafting predictive models to automating workflows, I bring ideas to life with data. Always innovating, always learning—I'm here to make technology work smarter, not harder, for everyone.")

    # Fun Fact Display
    st.info("""
    **Did You Know?**  
    Mayank means Moon 🌛
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
                        "name": "Auto-replenishment Engine",
                        "impacts": [
                            "✓ Deployed across 30+ brands",
                            "📉 Reduced replenishment frequency: 7 → 2 times weekly",
                            "📈 Increased store availability: 75% → >95%",
                            "💰 Generated AED 10M sales uplift in 2024",
                            "📊 Reduced loss of sale: 15% → 3%",
                            "💵 Saved AED 600K in labor costs"
                        ]
                    },
                    {
                        "name": "RITUALS Demand Forecasting Engine",
                        "impacts": [
                            "📈 Improved forecast accuracy: 56% → >80%",
                            "⚡ Reduced forecasting time: 16 hours → 2 hours",
                            "🤖 Implemented ML-driven approach for forecasting, replacing traditional ROS"
                        ]
                    },
                    {
                        "name": "Supply Chain Solutions Platform",
                        "impacts": [
                            "🔄 Centralized platform for replenishment, allocation, and pricing using Looker Studio",
                            "📊 Real-time 10+ KPI monitoring",
                            "📈 Increased solution adoption across brands"
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
                        "name": "Inventory & Distribution Dashboard",
                        "impacts": [
                            "📊 Real-time stock and logistics visibility",
                            "📈 Enhanced decision-making with trend analysis"
                        ]
                    },
                    {
                        "name": "Auto Inter-store Transfer Engine",
                        "impacts": [
                            "⚡ Reduced task completion: 8 hours → 30 minutes",
                            "💰 Generated 2-3% sales uplift",
                            "📈 Improved operational efficiency"
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
                        "name": "Water Quality Prediction Engine",
                        "impacts": [
                            "🤖 Developed pH, chlorine, and algae level prediction using XGBoost",
                            "📈 Enhanced user decision-making for pool cleaning"
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
                        "name": "Product Classification Model",
                        "impacts": [
                            "⚡ Reduced classification time: 8 hours → 20 minutes",
                            "📊 Achieved 88% accuracy in global name mapping"
                        ]
                    },
                    {
                        "name": "Social Media Risk Monitoring",
                        "impacts": [
                            "🔍 Built Tweet tracking module using Python Dash",
                            "📈 Enhanced product launch sentiment analysis"
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
