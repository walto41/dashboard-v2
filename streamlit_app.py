import streamlit as st
import pandas as pd
import plost

# Set the page layout and initial sidebar state
st.set_page_config(layout='wide', initial_sidebar_state='expanded')

# Load custom CSS for styling
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Sidebar for product categories and subcategories
st.sidebar.header('Product Dashboard')

st.sidebar.subheader('Product Categories')
product_category = st.sidebar.selectbox('Select Category', ('Electronics', 'Home Appliances', 'Fashion', 'Cooking'))

st.sidebar.subheader('Subcategories')
product_subcategory = st.sidebar.selectbox('Select Subcategory', ('Computers', 'Phones', 'Cameras', 'Kitchen Tools'))

# Footer in sidebar
st.sidebar.markdown('''
---
Created by Walter Patterson
''')

# Row A - Metrics for product performance
st.markdown('### Product Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", "$120K", "+10%")
col2.metric("Customer Satisfaction", "89%", "+2%")
col3.metric("Units Sold", "3.5K", "+5%")

# Row B - Data visualizations
sales_data = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv', parse_dates=['date'])
product_data = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv')

c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Sales Heatmap')
    plost.time_hist(
        data=product_data,
        date='date',
        x_unit='week',
        y_unit='day',
        color=product_category,
        aggregate='median',
        legend=None,
        height=345,
        use_container_width=True
    )
with c2:
    st.markdown('### Category Donut Chart')
    plost.donut_chart(
        data=sales_data,
        theta=product_subcategory,
        color='company',
        legend='bottom', 
        use_container_width=True
    )

# Row C - Line chart for sales trend
st.markdown('### Sales Trend Line Chart')
plot_data = sales_data[['date', 'price']]  # Replace with actual sales data columns
plot_height = 300
st.line_chart(plot_data, x='date', y='price', height=plot_height)
