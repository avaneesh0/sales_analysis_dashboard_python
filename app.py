import streamlit as st 
from src.data_loader import loadData
from PIL import Image
from src.visualization import (sales_per_quarter, 
                               sales_per_year,
                               sales_per_product,
                               sales_per_country,
                               sales_per_month
                               )

@st.cache_data
def get_data():
    return loadData()

sales_data = get_data()
filter_data = sales_data.copy()

img = Image.open("assets/images/money.webp")

st.set_page_config(layout="wide",
                   page_title="Sales analysis dashboard",
                   page_icon=img)

st.title("Sales Analytics Dashboard")
st.caption("Analyze sales performance across time, products, and regions")
st.divider()

st.sidebar.header("🔎 Filters")
year = st.sidebar.selectbox("📅 Select Year", ["All"] + sorted(sales_data["YEAR_ID"].unique()))
product = st.sidebar.selectbox("📦 Select Product", ["All"] + sorted(sales_data["PRODUCTLINE"].unique()))
Country = st.sidebar.selectbox("🌍 Select Country", ["All"] + sorted(sales_data["COUNTRY"].unique()))

if year != "All":
    filter_data = filter_data[filter_data["YEAR_ID"] == year]

if product != "All":
    filter_data = filter_data[filter_data["PRODUCTLINE"] == product]

if Country != "All":
    filter_data = filter_data[filter_data["COUNTRY"] == Country]

col1, col2, col3 = st.columns(3)

col1.metric(" 💰 Total sales", f"${filter_data['SALES'].sum():,.0f}")
col2.metric(" 📦 Total order", f"{filter_data.shape[0]:,}")
col3.metric(" 📊 Average order value", f"${filter_data['SALES'].mean():,.0f}")

st.divider()

with st.container():
    st.subheader("📈 Sales Trend Over Time")
    
    mainfig = sales_per_month(sales_data, year, Country, product)
    st.plotly_chart(mainfig, use_container_width=True)
    st.divider()
    
    col4, col5 = st.columns(2)
    fig1 = sales_per_quarter(sales_data , year, Country, product)
    fig2 = sales_per_year(sales_data, Country, product)

    with col4:
        st.plotly_chart(fig1, use_container_width=True)
        
    with col5:
        st.plotly_chart(fig2, use_container_width=True)
        st.info("-2005 is from january-may")


st.divider()

with st.container():
    st.subheader("📊Distribution Insights")
    
    col6, col7 = st.columns(2)
    fig3 = sales_per_product(sales_data , year, Country)
    fig4 = sales_per_country(sales_data , year, Country, product)
        
    with col6:
        st.plotly_chart(fig3, use_container_width=True)
    with col7:
        st.plotly_chart(fig4, use_container_width=True)

st.divider()

with st.expander("View Data"):
    st.dataframe(filter_data)

st.download_button(
    label="📥 Download Filtered Data",
    data=filter_data.to_csv(index=False),
    file_name="filtered_sales.csv",
    mime="text/csv"
)
st.divider()
st.caption("Built with Streamlit & Plotly | Data Analytics Project")
st.caption("Developer Avaneesh singh")