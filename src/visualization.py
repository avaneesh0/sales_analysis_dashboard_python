import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
# from data_loader import loadData

# data = loadData()
# print(data)

# sales per quaters bar 
def sales_per_quater(df: pd.DataFrame):
    data = df.groupby(["YEAR_ID", "QTR_ID"])["SALES"].sum().reset_index()
    data["year-quater"] = data["YEAR_ID"].astype(str) + "-Q" + data["QTR_ID"].astype(str)
    fig = px.bar(data, x="year-quater", y="SALES")
    return fig

# sales per years bar
def sales_per_year(df: pd.DataFrame):
    data = df.groupby("YEAR_ID")["SALES"].sum().reset_index()
    fig = px.bar(data, x="YEAR_ID", y="SALES")
    return fig

# sales per product line bar
def sales_per_product(df: pd.DataFrame):
    data = df.groupby("PRODUCTLINE")["SALES"].sum().sort_values().reset_index()
    fig = px.bar(data, x="PRODUCTLINE", y="SALES")
    return fig
    
# sales per country
def sales_per_country(df: pd.DataFrame):
    data = df.groupby("COUNTRY")["SALES"].sum().sort_values().reset_index()
    fig = px.bar(data, x="COUNTRY", y="SALES")
    return fig

# sales per month
def sales_per_month(df: pd.DataFrame):
    data = df.groupby(["YEAR_ID", "MONTH_ID"])["SALES"].sum().reset_index()
    data["year-month"] = data["YEAR_ID"].astype(str) + "-" +  data["MONTH_ID"].astype(str)
    fig = px.line(data, x="year-month", y="SALES")
    return fig