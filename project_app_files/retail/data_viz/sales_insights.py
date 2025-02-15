import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import numpy as np
from scipy import stats
import os

def show_dashboard():
    try:
        # Add Back Button
        col1, col2 = st.columns([1, 11])
        with col1:
            if st.button("← Back"):
                st.switch_page("pages/projects.py")
        with col2:
            st.title("📊 Retail Sales Analytics Dashboard")
        
        st.markdown("*An interactive dashboard for analyzing retail sales performance*")
        st.markdown("---")

        # Custom CSS for better UI
        st.markdown("""
            <style>
            .main {
                padding: 0rem 1rem;
            }
            .stMetric {
                background-color: #f0f2f6;
                padding: 15px;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            h1, h2, h3 {
                color: #1f77b4;
            }
            .stSidebar {
                background-color: #f8f9fa;
                padding: 1rem;
            }
            .insight-card {
                background-color: #ffffff;
                padding: 1rem;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                margin-bottom: 1rem;
            }
            </style>
        """, unsafe_allow_html=True)

        # Get the current file's directory and construct relative path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(current_dir, "retail_sales_dataset.csv")
        df = pd.read_csv(data_path)
        
        # Data Preprocessing
        df['Date'] = pd.to_datetime(df['Date'])
        df['Year'] = df['Date'].dt.year
        df = df[df['Year'] != 2024]
        df['Month'] = df['Date'].dt.month
        df['Month_Name'] = df['Date'].dt.strftime('%B')
        df['YearMonth'] = df['Date'].dt.strftime('%Y-%m')

        # Create a month order dictionary for sorting
        month_order = {
            'January': 1, 'February': 2, 'March': 3, 'April': 4,
            'May': 5, 'June': 6, 'July': 7, 'August': 8,
            'September': 9, 'October': 10, 'November': 11, 'December': 12
        }

        # Sidebar Filters
        with st.sidebar:
            st.header("📌 Dashboard Filters")
            st.markdown("---")
            
            # Month filter with proper chronological sorting
            available_months = df['Month_Name'].unique().tolist()
            sorted_months = sorted(available_months, key=lambda x: month_order[x])
            months = ['All'] + sorted_months
            selected_month = st.selectbox("📅 Select Month", months)
            
            # Product Category filter
            categories = ['All'] + sorted(df['Product Category'].unique().tolist())
            selected_category = st.selectbox("📦 Select Product Category", categories)
            
            # Gender filter
            genders = ['All'] + sorted(df['Gender'].unique().tolist())
            selected_gender = st.selectbox("👤 Select Gender", genders)

            # Age Range filter
            age_ranges = ['All', '18-25', '26-35', '36-45', '46-55', '55+']
            selected_age = st.selectbox("👥 Select Age Range", age_ranges)

        # Filter Data
        filtered_df = df.copy()
        
        if selected_month != 'All':
            filtered_df = filtered_df[filtered_df['Month_Name'] == selected_month]
        if selected_category != 'All':
            filtered_df = filtered_df[filtered_df['Product Category'] == selected_category]
        if selected_gender != 'All':
            filtered_df = filtered_df[filtered_df['Gender'] == selected_gender]
        if selected_age != 'All':
            age_ranges = {
                '18-25': (18, 25),
                '26-35': (26, 35),
                '36-45': (36, 45),
                '46-55': (46, 55),
                '55+': (55, 200)
            }
            age_min, age_max = age_ranges[selected_age]
            filtered_df = filtered_df[(filtered_df['Age'] >= age_min) & (filtered_df['Age'] <= age_max)]

        # Helper function to format currency in K
        def format_currency(value):
            if value >= 1000:
                return f"${value/1000:.1f}K"
            return f"${value:.2f}"

        # KPI Metrics Calculation
        total_sales = filtered_df['Total Amount'].sum()
        total_quantity = filtered_df['Quantity'].sum()
        avg_price = filtered_df['Price per Unit'].mean()
        total_customers = filtered_df['Customer ID'].nunique()
        avg_order_value = filtered_df.groupby('Transaction ID')['Total Amount'].sum().mean()

        # Display KPI Metrics
        st.subheader("📈 Key Performance Indicators")
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.metric(
                "Total Sales",
                format_currency(total_sales),
                None
            )
        
        with col2:
            st.metric(
                "Total Quantity Sold",
                f"{total_quantity:,}",
                None
            )
        
        with col3:
            st.metric(
                "Average Price",
                f"${avg_price:.2f}",
                None
            )
        
        with col4:
            st.metric(
                "Unique Customers",
                f"{total_customers:,}",
                None
            )
        
        with col5:
            st.metric(
                "Avg Order Value",
                format_currency(avg_order_value),
                None
            )

        # After KPI Metrics display
        st.markdown("---")
        
        # Create tabs
        tab1, tab2 = st.tabs(["📊 Univariate Analysis", "🔄 Multivariate Analysis"])
        
        with tab1:
            st.subheader("Sales Trend Analysis")
            col1, col2 = st.columns(2)

            with col1:
                # Monthly Sales Trend
                monthly_sales = df.groupby(['Year', 'Month', 'Month_Name'])['Total Amount'].sum().reset_index()
                monthly_sales = monthly_sales.sort_values(['Year', 'Month'])
                monthly_sales['Year'] = monthly_sales['Year'].astype(str)
                monthly_sales['Total Amount'] = monthly_sales['Total Amount'] / 1000
                
                # Create sequential index for trendline calculation
                monthly_sales['Index'] = range(len(monthly_sales))
                
                # Create the base line plot
                fig_monthly = px.line(monthly_sales, 
                                    x='Month_Name', 
                                    y='Total Amount',
                                    color='Year',
                                    title='Monthly Sales Trend by Year',
                                    template='presentation',
                                    markers=True)
                
                # Calculate OLS trendline
                slope, intercept, r_value, p_value, std_err = stats.linregress(monthly_sales['Index'], monthly_sales['Total Amount'])
                line = slope * monthly_sales['Index'] + intercept
                
                # Add OLS trendline
                fig_monthly.add_trace(
                    go.Scatter(
                        x=monthly_sales['Month_Name'],
                        y=line,
                        name=f'Trend (R² = {r_value**2:.3f})',
                        line=dict(color='red', dash='dash'),
                        showlegend=True
                    )
                )

                fig_monthly.update_layout(
                    height=500,
                    xaxis_title="Month",
                    yaxis_title="Sales (K$)",
                    hovermode='x unified',
                    legend_title="Year",
                    plot_bgcolor='white',
                    paper_bgcolor='white',
                    xaxis=dict(showgrid=False, title_font=dict(size=14), tickfont=dict(size=12)),
                    yaxis=dict(showgrid=False, title_font=dict(size=14), tickfont=dict(size=12)),
                    legend=dict(font=dict(size=12)),
                    title=dict(font=dict(size=16))
                )
                
                month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                              'July', 'August', 'September', 'October', 'November', 'December']
                fig_monthly.update_xaxes(categoryorder='array', categoryarray=month_order)
                
                # Add annotation for trend direction and significance
                trend_direction = "Upward" if slope > 0 else "Downward"
                significance = "Significant" if p_value < 0.05 else "Not Significant"
                fig_monthly.add_annotation(
                    text=f"{trend_direction} Trend ({significance})<br>R² = {r_value**2:.3f}",
                    xref="paper", yref="paper",
                    x=0.02, y=0.98,
                    showarrow=False,
                    font=dict(size=12, color="red"),
                    bgcolor="white",
                    bordercolor="red",
                    borderwidth=1
                )
                st.plotly_chart(fig_monthly, use_container_width=True)

            with col2:
                # Category Performance by Year
                category_sales = filtered_df.groupby(['Year', 'Product Category']).agg({
                    'Total Amount': 'sum',
                    'Quantity': 'sum'
                }).reset_index()
                category_sales['Year'] = category_sales['Year'].astype(str)
                # Convert to thousands
                category_sales['Total Amount'] = category_sales['Total Amount'] / 1000
                
                fig_category = px.bar(category_sales,
                                    x='Product Category',
                                    y='Total Amount',
                                    color='Year',
                                    title='Product Category Performance by Year',
                                    template='presentation',
                                    barmode='stack')
                
                # Add line for Quantity on secondary axis with matching colors
                for idx, year in enumerate(category_sales['Year'].unique()):
                    year_data = category_sales[category_sales['Year'] == year]
                    fig_category.add_trace(
                        go.Scatter(
                            x=year_data['Product Category'],
                            y=year_data['Quantity'],
                            name=f'Quantity {year}',
                            yaxis='y2',
                            line=dict(
                                color=px.colors.sequential.Blues[2:][idx],
                                dash='dot',
                                width=2
                            ),
                            mode='lines+markers'
                        )
                    )
                
                fig_category.update_layout(
                    yaxis=dict(
                        title='Sales (K$)',
                        showgrid=False,
                        title_font=dict(size=14),
                        tickfont=dict(size=12)
                    ),
                    yaxis2=dict(
                        title='Quantity',
                        overlaying='y',
                        side='right',
                        showgrid=False,
                        title_font=dict(size=14),
                        tickfont=dict(size=12)
                    ),
                    xaxis=dict(
                        showgrid=False,
                        title_font=dict(size=14),
                        tickfont=dict(size=12)
                    ),
                    hovermode='x unified',
                    height=500,
                    legend_title="Year",
                    plot_bgcolor='white',
                    paper_bgcolor='white',
                    legend=dict(font=dict(size=12)),
                    title=dict(font=dict(size=16))
                )
                st.plotly_chart(fig_category, use_container_width=True)

            st.subheader("Customer Demographics")
            col1, col2 = st.columns(2)

            with col1:
                # Gender Distribution by Year
                gender_sales = filtered_df.groupby(['Year', 'Gender'])['Total Amount'].sum().reset_index()
                gender_sales['Year'] = gender_sales['Year'].astype(str)
                
                # Calculate percentage for each year
                total_by_year = gender_sales.groupby('Year')['Total Amount'].transform('sum')
                gender_sales['Percentage'] = (gender_sales['Total Amount'] / total_by_year) * 100
                
                fig_gender = px.bar(gender_sales, 
                                  x='Gender',
                                  y='Percentage',
                                  color='Year',
                                  title='Sales Distribution by Gender (%)',
                                  template='presentation',
                                  barmode='group',
                                  text=gender_sales['Percentage'].round(1).astype(str) + '%')
                
                fig_gender.update_layout(
                    legend_title="Year",
                    plot_bgcolor='white',
                    paper_bgcolor='white',
                    yaxis_title="Percentage of Sales",
                    xaxis_title="Gender",
                    xaxis=dict(showgrid=False, title_font=dict(size=14), tickfont=dict(size=12)),
                    yaxis=dict(showgrid=False, title_font=dict(size=14), tickfont=dict(size=12)),
                    legend=dict(font=dict(size=12)),
                    title=dict(font=dict(size=16)),
                    font=dict(size=12)  # For the percentage labels on bars
                )
                st.plotly_chart(fig_gender, use_container_width=True)

            with col2:
                # Age Distribution by Year
                age_bins = [0, 25, 35, 45, 55, 100]
                age_labels = ['18-25', '26-35', '36-45', '46-55', '55+']
                filtered_df['Age Group'] = pd.cut(filtered_df['Age'], bins=age_bins, labels=age_labels)
                age_sales = filtered_df.groupby(['Year', 'Age Group'])['Total Amount'].sum().reset_index()
                age_sales['Year'] = age_sales['Year'].astype(str)
                
                # Calculate percentage for each year
                total_by_year = age_sales.groupby('Year')['Total Amount'].transform('sum')
                age_sales['Percentage'] = (age_sales['Total Amount'] / total_by_year) * 100
                
                fig_age = px.bar(age_sales,
                                x='Age Group',
                                y='Percentage',
                                color='Year',
                                title='Sales Distribution by Age Group (%)',
                                template='presentation',
                                barmode='group',
                                text=age_sales['Percentage'].round(1).astype(str) + '%')
                
                fig_age.update_layout(
                    legend_title="Year",
                    plot_bgcolor='white',
                    paper_bgcolor='white',
                    yaxis_title="Percentage of Sales",
                    xaxis_title="Age Group",
                    xaxis=dict(showgrid=False, title_font=dict(size=14), tickfont=dict(size=12)),
                    yaxis=dict(showgrid=False, title_font=dict(size=14), tickfont=dict(size=12)),
                    legend=dict(font=dict(size=12)),
                    title=dict(font=dict(size=16)),
                    font=dict(size=12)  # For the percentage labels on bars
                )
                st.plotly_chart(fig_age, use_container_width=True)

            # Univariate Analysis Insights
            st.markdown("---")
            st.subheader("📈 Key Insights from Univariate Analysis")
            
            col1, col2 = st.columns(2)
            with col1:
                # Sales Trends Insights
                st.markdown("**Sales Trends:**")
                
                # Calculate month-on-month average growth rate
                monthly_sales = df.groupby(['Year', 'Month'])['Total Amount'].sum().reset_index()
                monthly_sales = monthly_sales.sort_values(['Year', 'Month'])
                monthly_sales['Previous'] = monthly_sales['Total Amount'].shift(1)
                monthly_sales['Growth'] = ((monthly_sales['Total Amount'] - monthly_sales['Previous']) / monthly_sales['Previous']) * 100
                avg_monthly_growth = monthly_sales['Growth'].mean()
                
                st.info(f"📈 Average Monthly Growth Rate: {avg_monthly_growth:.1f}%")
                
                # Best and Worst Performing Months
                monthly_sum = df.groupby('Month_Name')['Total Amount'].sum()
                best_month = monthly_sum.idxmax()
                worst_month = monthly_sum.idxmin()
                st.success(f"🌟 Best Performing Month: {best_month}")
                st.error(f"📉 Lowest Performing Month: {worst_month}")


            with col2:
                # Customer Demographics Insights
                st.markdown("**Demographics:**")
                # Gender Distribution
                gender_dist = filtered_df['Gender'].value_counts()
                majority_gender = gender_dist.index[0]
                gender_pct = (gender_dist.iloc[0] / gender_dist.sum() * 100)
                st.info(f"👥 Majority Customer Gender: {majority_gender} ({gender_pct:.1f}%)")
                
                # Age Distribution
                st.success(f"📊 Most Common Age Group: {filtered_df['Age Group'].mode().iloc[0]}")
                st.error(f"🎯 Average Customer Age: {filtered_df['Age'].mean():.1f} years")

        with tab2:
            st.subheader("Multivariate Analysis")
            col1, col2 = st.columns(2)

            with col1:
                # Sales, Quantity, and Category by Gender
                gender_category_analysis = filtered_df.groupby(['Gender', 'Product Category']).agg({
                    'Total Amount': 'sum',
                    'Quantity': 'sum',
                    'Customer ID': 'nunique'
                }).reset_index()
                
                # Calculate average order value
                gender_category_analysis['Avg Order Value'] = gender_category_analysis['Total Amount'] / gender_category_analysis['Customer ID']
                
                fig_multi1 = px.scatter(gender_category_analysis,
                                      x='Total Amount',
                                      y='Quantity',
                                      size='Avg Order Value',
                                      color='Product Category',
                                      facet_col='Gender',
                                      title='Sales, Quantity & Category Distribution by Gender',
                                      template='presentation',
                                      labels={'Total Amount': 'Total Sales ($)',
                                             'Quantity': 'Units Sold'})
                
                fig_multi1.update_layout(
                    height=500,
                    showlegend=True,
                    plot_bgcolor='white',
                    paper_bgcolor='white'
                )
                st.plotly_chart(fig_multi1, use_container_width=True)

            with col2:
                # Age Group, Product Category, and Purchase Patterns
                age_pattern_analysis = filtered_df.groupby(['Age Group', 'Product Category', 'Gender']).agg({
                    'Total Amount': 'mean',
                    'Quantity': 'mean',
                    'Transaction ID': 'count'
                }).reset_index()
                
                fig_multi2 = px.scatter(age_pattern_analysis,
                                      x='Total Amount',
                                      y='Quantity',
                                      size='Transaction ID',
                                      color='Product Category',
                                      symbol='Gender',
                                      facet_col='Age Group',
                                      facet_col_wrap=2,
                                      title='Purchase Patterns by Age, Gender & Category',
                                      template='presentation')
                
                fig_multi2.update_layout(
                    height=500,
                    showlegend=True,
                    plot_bgcolor='white',
                    paper_bgcolor='white'
                )
                st.plotly_chart(fig_multi2, use_container_width=True)

            # Additional Multivariate Analysis
            col1, col2 = st.columns(2)

            with col1:
                # Time-based patterns with multiple variables
                time_patterns = filtered_df.groupby(['Year', 'Month_Name', 'Month', 'Product Category']).agg({
                    'Total Amount': 'sum',
                    'Quantity': 'mean',
                    'Customer ID': 'nunique'
                }).reset_index()
                
                time_patterns = time_patterns.sort_values(['Year', 'Month'])
                
                fig_multi3 = px.scatter(time_patterns,
                                      x='Total Amount',
                                      y='Customer ID',
                                      size='Quantity',
                                      color='Product Category',
                                      facet_col='Year',
                                      hover_data=['Month_Name'],
                                      title='Temporal Purchase Patterns',
                                      template='presentation')
                
                fig_multi3.update_layout(
                    height=500,
                    showlegend=True,
                    plot_bgcolor='white',
                    paper_bgcolor='white'
                )
                st.plotly_chart(fig_multi3, use_container_width=True)

            with col2:
                # Customer Segmentation Analysis
                segment_analysis = filtered_df.groupby(['Age Group', 'Gender', 'Product Category']).agg({
                    'Total Amount': ['mean', 'count'],
                    'Quantity': 'mean'
                }).reset_index()
                
                segment_analysis.columns = ['Age Group', 'Gender', 'Product Category', 'Avg Purchase', 'Purchase Frequency', 'Avg Quantity']
                
                fig_multi4 = px.sunburst(segment_analysis,
                                       path=['Gender', 'Age Group', 'Product Category'],
                                       values='Purchase Frequency',
                                       color='Avg Purchase',
                                       title='Customer Segmentation Analysis',
                                       template='presentation')
                
                fig_multi4.update_layout(
                    height=500,
                    plot_bgcolor='white',
                    paper_bgcolor='white'
                )
                st.plotly_chart(fig_multi4, use_container_width=True)

            # Multivariate Analysis Insights
            st.markdown("---")
            st.subheader("🔍 Key Insights from Multivariate Analysis")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Customer Segmentation Insights:**")
                
                # Find highest value segment
                top_segment = segment_analysis.nlargest(1, 'Avg Purchase')
                st.info(f"💎 Highest Value Segment:\n"
                       f"- Gender: {top_segment['Gender'].iloc[0]}\n"
                       f"- Age Group: {top_segment['Age Group'].iloc[0]}\n"
                       f"- Category: {top_segment['Product Category'].iloc[0]}\n"
                       f"- Avg Purchase: ${top_segment['Avg Purchase'].iloc[0]:.2f}")
                
                # Most frequent purchasing segment
                frequent_segment = segment_analysis.nlargest(1, 'Purchase Frequency')
                st.success(f"🔄 Most Active Segment:\n"
                          f"- Gender: {frequent_segment['Gender'].iloc[0]}\n"
                          f"- Age Group: {frequent_segment['Age Group'].iloc[0]}\n"
                          f"- Category: {frequent_segment['Product Category'].iloc[0]}\n"
                          f"- Purchase Frequency: {frequent_segment['Purchase Frequency'].iloc[0]:.0f}")

            with col2:
                st.markdown("**Pattern Analysis:**")
                
                # Calculate category performance by gender and age
                category_performance = filtered_df.groupby('Product Category').agg({
                    'Total Amount': ['mean', 'count'],
                    'Quantity': 'mean'
                }).reset_index()
                
                # Find best performing category overall
                best_category = category_performance.nlargest(1, ('Total Amount', 'mean'))
                st.info(f"📊 Best Performing Category:\n"
                       f"- Category: {best_category['Product Category'].iloc[0]}\n"
                       f"- Avg Purchase: ${best_category[('Total Amount', 'mean')].iloc[0]:.2f}\n"
                       f"- Avg Quantity: {best_category[('Quantity', 'mean')].iloc[0]:.1f}")
                
                # Time-based insights
                time_insights = filtered_df.groupby(['Year', 'Month'])['Total Amount'].agg(['mean', 'count']).reset_index()
                peak_time = time_insights.nlargest(1, 'mean')
                st.success(f"⏰ Peak Shopping Period:\n"
                          f"- Year: {peak_time['Year'].iloc[0]}\n"
                          f"- Month: {peak_time['Month'].iloc[0]}\n"
                          f"- Avg Purchase: ${peak_time['mean'].iloc[0]:.2f}\n"
                          f"- Transaction Count: {peak_time['count'].iloc[0]:.0f}")

    except Exception as e:
        st.error(f"Error loading or processing data: {str(e)}")
        st.info("Please check if the dataset file exists and is accessible.")
        return

if __name__ == "__main__":
    show_dashboard()