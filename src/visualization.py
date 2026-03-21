import pandas as pd
import plotly.express as px

# sales per quaters bar 
def sales_per_quater(df: pd.DataFrame, year):
    if year == "All":
        data = (df.groupby(["YEAR_ID", "QTR_ID"])["SALES"]
                .sum()
                .reset_index()
                )
        data["year-quarter"] = "Q" + data["QTR_ID"].astype(str) + "-"+ data["YEAR_ID"].astype(str)
        fig = px.bar(data, 
                    x="year-quarter", 
                    y="SALES",
                    height=350,
                    width=500,
                    labels={"year-quarter": "Quarter", 
                            "SALES": "Sales"}
                    )
        return fig
    else:
        filtered_df = df[df["YEAR_ID"] == year]
        data = (filtered_df.groupby("QTR_ID")["SALES"]
                .sum()
                .reset_index()
                )
        data["year-quarter"] = "Q" + data["QTR_ID"].astype(str) + "-" +  year.astype(str)
        fig = px.bar(data, 
                    x="year-quarter", 
                    y="SALES",
                    height=450,
                    width=600,
                    labels={"year-quarter": "Quarter", 
                            "SALES": "Sales"}
                    )
        return fig

# sales per years bar
def sales_per_year(df: pd.DataFrame, year):
    
    data = (df.groupby("YEAR_ID")["SALES"]
            .sum()
            .reset_index()
            )
    fig = px.bar(data, 
                 x="YEAR_ID", 
                 y="SALES",
                 height=450,
                 width=500,
                 labels={"YEAR_ID": "Year", 
                         "SALES": "Sales"}
                 )
    return fig

# sales per product line bar
def sales_per_product(df: pd.DataFrame, year):
    if year != "All":
        data = (df[df["YEAR_ID"] == year]
                .groupby("PRODUCTLINE")["SALES"]
                .sum()
                .sort_values()
                .reset_index()
                )
    else:
        data = (df.groupby("PRODUCTLINE")["SALES"]
                .sum()
                .sort_values()
                .reset_index()
                )
    fig = px.pie(data, 
                 names="PRODUCTLINE",
                 values="SALES",
                 height=430,
                 width=500,
                )
    return fig
    
# sales per country
def sales_per_country(df: pd.DataFrame, year):
    if year != "All":
        data = (df[df["YEAR_ID"] == year]
                .groupby("COUNTRY")["SALES"]
                .sum()
                .sort_values()
                .reset_index()
                )
    else:
        data = (df.groupby("COUNTRY")["SALES"]
                .sum()
                .sort_values()
                .reset_index()
                )
    fig = px.bar(data, 
                 x="SALES",
                 y="COUNTRY", 
                 height=450,
                 width=500,
                 orientation="h",
                 labels={"COUNTRY": "Countrys", "SALES": "Sales"})
    return fig

# sales per month
def sales_per_month(df: pd.DataFrame, year):
    if year == "All":
        data = (df.groupby(["YEAR_ID", "MONTH_ID"])["SALES"]
                .sum()
                .reset_index()
                )
        data["year-month"] = data["YEAR_ID"].astype(str) + "-" +  data["MONTH_ID"].astype(str)
        fig = px.line(data, 
                    x="year-month", 
                    y="SALES",
                    height=350,
                    width=500,
                    labels={"year-month": "Month-Year", "SALES": "Sales"})
        return fig
    else:
        filtered_df = df[df["YEAR_ID"] == year]
        data = (filtered_df.groupby("MONTH_ID")["SALES"]
                .sum()
                .reset_index()
                )
        data["year-month"] = year.astype(str) + "-" +  data["MONTH_ID"].astype(str)
        fig = px.line(data, 
                    x="year-month", 
                    y="SALES",
                    height=350,
                    width=500,
                    labels={"year-month": "Month-Year", "SALES": "Sales"})
        return fig
    
    