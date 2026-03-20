import streamlit as st 
from src.data_loader import loadData
from src.visualization import (sales_per_quater, 
                               sales_per_year,
                               sales_per_product,
                               sales_per_country,
                               sales_per_month)

sales_data = loadData()

st.set_page_config(layout="wide")

st.title("Sales Analytics Dashboard")
st.markdown("Analyze sales performance across time, product lines, and regions.")

st.sidebar.header("🔎 Filters")
year = st.sidebar.selectbox("Select Year", ["All"] + sorted(sales_data["YEAR_ID"].unique()))
product = st.sidebar.selectbox("Select Product", ["All"] + sorted(sales_data["PRODUCTLINE"].unique()))

col1, col2, col3 = st.columns(3)

col1.metric(" 💰 Total sales", f"${sales_data['SALES'].sum():,.0f}")
col2.metric(" 📦 Total order", f"{sales_data.shape[0]:,}")
col3.metric(" 📊 Average order value", f"${sales_data['SALES'].mean():,.0f}")

st.markdown("----")

mainfig = sales_per_month(sales_data, year)
st.subheader("📈 Monthly Sales Trend")
st.plotly_chart(mainfig, use_container_width=True)

st.markdown("----")

col4, col5 = st.columns(2)
fig1 = sales_per_quater(sales_data , year)
fig2 = sales_per_product(sales_data , year)

with col4:
    st.subheader("📅 Quarterly Sales Distribution")
    st.plotly_chart(fig1, use_container_width=True)
with col5:
    st.subheader("📊 Sales by Product Line")
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("----")

col6, col7 = st.columns(2)
fig3 = sales_per_country(sales_data , year)
fig4 = sales_per_year(sales_data , year)

with col6:
    st.subheader("🌍 Sales by Country")
    st.plotly_chart(fig3, use_container_width=True)
with col7:
    st.subheader("📅 Sales per Year ")
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("----")

with st.expander("View Data"):
    st.dataframe(sales_data)

st.markdown("----")    
st.caption("Built with Streamlit & Plotly | Data Analytics Project")