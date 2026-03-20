import streamlit as st 
import pandas as pd
from src.data_loader import loadData
from src.visualization import (sales_per_quater, 
                               sales_per_year,
                               sales_per_product,
                               sales_per_country,
                               sales_per_month)

sales_data = loadData()

st.title("Sales Analytics Dashboard")

year = st.sidebar.selectbox("Year", sales_data["YEAR_ID"].unique())
product = st.sidebar.selectbox("Product", sales_data["PRODUCTLINE"].unique())

col1, col2, col3 = st.columns(3)

col1.metric("Total sales", f"${sales_data["SALES"].sum():.0f}")
col2.metric("Total order", sales_data["QUANTITYORDERED"].sum())
col3.metric("Average order value", f"${sales_data["SALES"].mean():.0f}")

mainfig = sales_per_month(sales_data)
st.subheader("sales per month")
st.plotly_chart(mainfig)

col4, col5 = st.columns(2)
fig1 = sales_per_quater(sales_data)
fig2 = sales_per_product(sales_data)

with col4:
    st.subheader("sales per quater")
    st.plotly_chart(fig1, use_container_width=True)
with col5:
    st.subheader("sales by product")
    st.plotly_chart(fig2, use_container_width=True)
    
col6, col7 = st.columns(2)
fig3 = sales_per_country(sales_data)
fig4 = sales_per_year(sales_data)

with col6:
    st.subheader("sales per country")
    st.plotly_chart(fig3, use_container_width=True)
with col7:
    st.subheader("sales per year ")
    st.plotly_chart(fig4, use_container_width=True)
    
with st.expander("View data"):
    st.dataframe(sales_data)