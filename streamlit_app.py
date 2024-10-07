import streamlit as st
import pandas as pd
import numpy as np
import plost
import datetime

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

# Generate random sales data
np.random.seed(42)
dates = pd.date_range(start="2023-01-01", periods=100)
sales_data = pd.DataFrame({
    'date': dates,
    'price': np.random.uniform(10, 500, size=(100,)),
    'category': np.random.choice(['Electronics', 'Home Appliances', 'Fashion', 'Cooking'], size=100),
    'company': np.random.choice(['Company A', 'Company B', 'Company C'], size=100)
})

# Generate random product data
product_data = pd.DataFrame({
    'date': dates,
    'sales': np.random.randint(50, 300, size=(100,)),
    'category': np.random.choice(['Computers', 'Phones', 'Cameras', 'Kitchen Tools'], size=100)
})



# Row C - Line chart for sales trend
st.markdown('### Sales Trend Line Chart')

# Plot the sales trend line chart with random data
plot_data = sales_data[['date', 'price']]
plot_height = 300
st.line_chart(plot_data, x='date', y='price', height=plot_height)
