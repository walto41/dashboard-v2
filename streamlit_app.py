import streamlit as st
import pandas as pd
import numpy as np
import plost

# Ensure this is the first Streamlit command in your script
st.set_page_config(layout='wide', initial_sidebar_state='expanded')

# Load custom CSS for styling
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Sidebar configuration
st.sidebar.header('Product Dashboard')

# Rest of y

# Sidebar parameters
st.sidebar.subheader('Heatmap parameter')
heatmap_color = st.sidebar.selectbox('Color by', ('category', 'company'))

st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('Select data', ('category', 'company'))

st.sidebar.subheader('Line chart parameters')
line_chart_data = st.sidebar.multiselect('Select data', ['price', 'sales'], ['price', 'sales'])
line_chart_height = st.sidebar.slider('Specify plot height', 200, 500, 300)

st.sidebar.markdown('''
---
Created by Walter Patterson
''')

# Generate random sales data
np.random.seed(42)
dates = pd.date_range(start="2023-01-01", periods=100)
sales_data = pd.DataFrame({
    'date': dates,
    'price': np.random.uniform(10, 500, size=(100,)),
    'sales': np.random.randint(50, 300, size=(100,)),
    'category': np.random.choice(['Electronics', 'Home Appliances', 'Fashion', 'Cooking'], size=100),
    'company': np.random.choice(['Company A', 'Company B', 'Company C'], size=100)
})

# Row A - Metrics
st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${sales_data['price'].sum():,.2f}", "+5%")
col2.metric("Units Sold", f"{sales_data['sales'].sum():,}", "+7%")
col3.metric("Top Category", sales_data['category'].mode()[0])

# Row B - Visualizations
c1, c2 = st.columns((7, 3))
with c1:
    st.markdown('### Heatmap')
    plost.time_hist(
        data=sales_data,
        date='date',
        x_unit='week',
        y_unit='day',
        color=heatmap_color,
        aggregate='median',
        legend=None,
        height=345,
        use_container_width=True
    )
with c2:
    st.markdown('### Donut Chart')
    plost.donut_chart(
        data=sales_data,
        theta=donut_theta,
        color='company',
        legend='bottom',
        use_container_width=True
    )

# Row C - Line Chart
st.markdown('### Line Chart')
if line_chart_data:
    st.line_chart(sales_data[['date'] + line_chart_data].set_index('date'), height=line_chart_height)
else:
    st.warning("Please select at least one data point for the line chart.")

import plost

# Set the page layout and initial sidebar state
st.set_page_config(layout='wide', initial_sidebar_state='expanded')

# Load custom CSS for styling
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Sidebar configuration
st.sidebar.header('Product Dashboard')

# Sidebar parameters
st.sidebar.subheader('Heatmap parameter')
heatmap_color = st.sidebar.selectbox('Color by', ('category', 'company'))

st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('Select data', ('category', 'company'))

st.sidebar.subheader('Line chart parameters')
line_chart_data = st.sidebar.multiselect('Select data', ['price', 'sales'], ['price', 'sales'])
line_chart_height = st.sidebar.slider('Specify plot height', 200, 500, 300)

st.sidebar.markdown('''
---
Created by Walter Patterson
''')

# Generate random sales data
np.random.seed(42)
dates = pd.date_range(start="2023-01-01", periods=100)
sales_data = pd.DataFrame({
    'date': dates,
    'price': np.random.uniform(10, 500, size=(100,)),
    'sales': np.random.randint(50, 300, size=(100,)),
    'category': np.random.choice(['Electronics', 'Home Appliances', 'Fashion', 'Cooking'], size=100),
    'company': np.random.choice(['Company A', 'Company B', 'Company C'], size=100)
})

# Row A - Metrics
st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${sales_data['price'].sum():,.2f}", "+5%")
col2.metric("Units Sold", f"{sales_data['sales'].sum():,}", "+7%")
col3.metric("Top Category", sales_data['category'].mode()[0])

# Row B - Visualizations
c1, c2 = st.columns((7, 3))
with c1:
    st.markdown('### Heatmap')
    plost.time_hist(
        data=sales_data,
        date='date',
        x_unit='week',
        y_unit='day',
        color=heatmap_color,
        aggregate='median',
        legend=None,
        height=345,
        use_container_width=True
    )
with c2:
    st.markdown('### Donut Chart')
    plost.donut_chart(
        data=sales_data,
        theta=donut_theta,
        color='company',
        legend='bottom',
        use_container_width=True
    )

# Row C - Line Chart
st.markdown('### Line Chart')
if line_chart_data:
    st.line_chart(sales_data[['date'] + line_chart_data].set_index('date'), height=line_chart_height)
else:
    st.warning("Please select at least one data point for the line chart.")
