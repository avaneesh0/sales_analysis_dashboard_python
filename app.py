import streamlit as st 
import pandas as pd
from src.data_loader import loadData
from src.visualization import (sales_per_quater, 
                               sales_per_year,
                               sales_per_product)

sales_data = loadData()

st.title("Sales Analytics Dashboard")

year = st.sidebar.selectbox("Year", sales_data["YEAR_ID"].unique())
product = st.sidebar.selectbox("Product", sales_data["PRODUCTLINE"].unique())

col1, col2, col3 = st.columns(3)

col1.metric("Total sales", f"${sales_data["SALES"].sum():.0f}")
col2.metric("Total order", sales_data["QUANTITYORDERED"].sum())
col3.metric("Average order value", f"${sales_data["SALES"].mean():.0f}")

fig1 = sales_per_quater(sales_data)
fig2 = sales_per_year(sales_data)
fig3 = sales_per_product(sales_data)
with col1:
    st.subheader("sales per quater")
    st.pyplot(fig1)
with col2:
    st.subheader("sales per year")
    st.pyplot(fig2)
with col3:
    st.subheader("sales by product")
    st.pyplot(fig3)
    
with st.expander("View data"):
    st.dataframe(sales_data)