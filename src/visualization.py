import pandas as pd
import plotly.express as px

# sales per quaters bar 
def sales_per_quarter(df: pd.DataFrame, year,country: str  , product: str):
    if year == "All":
        data = (df.groupby(["YEAR_ID", "QTR_ID"])["SALES"]
                .sum()
                .reset_index()
                )
        
        if product != "All":
                if country != "All":
                        product_filter = df[(df["PRODUCTLINE"] == product) & (df["COUNTRY"] == country)]
                else:
                        product_filter = df[df["PRODUCTLINE"] == product]
                        
                data = (product_filter.groupby(["YEAR_ID", "QTR_ID"])["SALES"]
                .sum()
                .reset_index()
                )
                
        if country != "All":
                if product != "All":
                        product_filter = df[(df["PRODUCTLINE"] == product) & (df["COUNTRY"] == country)]
                else:
                        product_filter = df[df["COUNTRY"] == country]
                        
                data = (product_filter.groupby(["YEAR_ID", "QTR_ID"])["SALES"]
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
                            "SALES": "Sales"},
                    title=" 📅 Quarterly Sales Distribution ",
                    )
        return fig

    else:
            
        filtered_df = df[df["YEAR_ID"] == year]
        data = (filtered_df.groupby("QTR_ID")["SALES"]
                .sum()
                .reset_index()
                )
        
        if product != "All":
                if country != "All":
                        product_filter = df[(df["PRODUCTLINE"] == product) & (df["YEAR_ID"] == year) & (df["COUNTRY"] == country)]
                else:
                        product_filter = df[(df["PRODUCTLINE"] == product) & (df["YEAR_ID"] == year)]
                data = (product_filter.groupby(["YEAR_ID", "QTR_ID"])["SALES"]
                        .sum()
                        .reset_index()
                        )
                
        if country != "All":
                if product != "All":
                        product_filter = df[(df["PRODUCTLINE"] == product) & (df["YEAR_ID"] == year) & (df["COUNTRY"] == country)]
                else:
                        product_filter = df[(df["YEAR_ID"] == year) & (df["COUNTRY"] == country)]
                
                data = (product_filter.groupby(["YEAR_ID", "QTR_ID"])["SALES"]
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
                        "SALES": "Sales"},
                title=" 📅 Quarterly Sales Distribution "
                )
        return fig

# sales per years bar
def sales_per_year(df: pd.DataFrame, country: str  , product: str):
        if product != "All":
                if country != "All":
                        product_filter = df[(df["PRODUCTLINE"] == product) & (df["COUNTRY"] == country)]
                else: 
                        product_filter = df[df["PRODUCTLINE"] == product]
                        
                data = (product_filter.groupby("YEAR_ID")["SALES"]
                        .sum()
                        .reset_index()
                        )
        else:
                if country != "All":
                        product_filter = df[df["COUNTRY"] == country]
                else:
                        product_filter = df
                data = (product_filter.groupby("YEAR_ID")["SALES"]
                .sum()
                .reset_index()
                )
        data["YEAR"] = "y - " + data["YEAR_ID"].astype(str) 
        fig = px.bar(data, 
                x="YEAR", 
                y="SALES",
                height=450,
                width=500,
                labels={"YEAR": "Year", 
                        "SALES": "Sales"},
                title="📅 Sales per Year "
                )
        return fig

# sales per product line bar
def sales_per_product(df: pd.DataFrame, year,country: str ):
    if year != "All":
        data = (df[df["YEAR_ID"] == year]
                .groupby("PRODUCTLINE")["SALES"]
                .sum()
                .sort_values()
                .reset_index()
                )
        if country != "All":
                data = (df[(df["YEAR_ID"] == year) & (df["COUNTRY"] == country)]
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
        if country != "All":
                data = (df[df["COUNTRY"] == country]
                .groupby("PRODUCTLINE")["SALES"]
                .sum()
                .sort_values()
                .reset_index()
                )
        
    fig = px.pie(data, 
        names="PRODUCTLINE",
        values="SALES",
        height=500,
        width=500,
        title="📊 Sales by Product Line"
        )
    return fig
    
# sales per country
def sales_per_country(df: pd.DataFrame, year,country: str  , product: str):
    if year != "All":
        data = (df[df["YEAR_ID"] == year]
                .groupby("COUNTRY")["SALES"]
                .sum()
                .sort_values()
                .reset_index()
                )
        if product != "All":
                product_filter = df[(df["PRODUCTLINE"] == product) & (df["YEAR_ID"] == year)]
                data = (product_filter
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
        if product != "All":
                product_filter = df[df["PRODUCTLINE"] == product]
                data = (product_filter
                        .groupby("COUNTRY")["SALES"]
                        .sum()
                        .sort_values()
                        .reset_index()
                        )
    highlighted_country = country
    data["COLOR"] = data["COUNTRY"].apply(lambda c: f"{country}" if c == highlighted_country else "Other")
    fig = px.bar(data, 
                 x="SALES",
                 y="COUNTRY",
                 color="COLOR",
                 color_discrete_map={f"{country}": "green", "Other": "skyblue"},
                 height=500,
                 width=500,
                 orientation="h",
                 labels={"COUNTRY": "Countrys", "SALES": "Sales"},
                 title="🌍 Sales by Country"
                 )
    return fig

# sales per month
def sales_per_month(df: pd.DataFrame, year,country: str  , product: str):
    if year == "All":
        data = (df.groupby(["YEAR_ID", "MONTH_ID"])["SALES"]
                .sum()
                .reset_index()
                )
        if product != "All":
                if country != "All":
                        product_filter = df[(df["PRODUCTLINE"] == product) & (df["COUNTRY"] == country)]
                else:
                        product_filter = df[df["PRODUCTLINE"] == product]
                data = (product_filter
                        .groupby(["YEAR_ID", "MONTH_ID"])["SALES"]
                        .sum()
                        .reset_index()
                        )
                
        if country != "All":
                if product != "All":
                        product_filter = df[(df["PRODUCTLINE"] == product) & (df["COUNTRY"] == country)]
                else:
                        product_filter = df[df["COUNTRY"] == country]
                data = (product_filter
                        .groupby(["YEAR_ID", "MONTH_ID"])["SALES"]
                        .sum()
                        .reset_index()
                        )
                
        data["year-month"] = data["YEAR_ID"].astype(str) + "-" +  data["MONTH_ID"].astype(str)
        fig = px.line(data, 
                    x="year-month", 
                    y="SALES",
                    height=350,
                    width=500,
                    labels={"year-month": "Month-Year", 
                            "SALES": "Sales"},
                    title="📈 Monthly Sales Trend",
                    )
        return fig
    else:
        filtered_df = df[df["YEAR_ID"] == year]
        data = (filtered_df.groupby("MONTH_ID")["SALES"]
                .sum()
                .reset_index()
                )
        if product != "All":
                if country != "All":
                        product_filter = df[(df["PRODUCTLINE"] == product) & (df["YEAR_ID"] == year) & (df["COUNTRY"] == country)]
                else:
                        product_filter = df[(df["PRODUCTLINE"] == product) & (df["YEAR_ID"] == year)]
                data = (product_filter
                        .groupby(["YEAR_ID", "MONTH_ID"])["SALES"]
                        .sum()
                        .reset_index()
                        )
                
        if country != "All":
                if product != "All":
                        product_filter = df[(df["PRODUCTLINE"] == product) & (df["YEAR_ID"] == year) & (df["COUNTRY"] == country)]
                else:
                        product_filter = df[(df["COUNTRY"] == country) & (df["YEAR_ID"] == year)]
                data = (product_filter
                        .groupby(["YEAR_ID", "MONTH_ID"])["SALES"]
                        .sum()
                        .reset_index()
                        )
        data["year-month"] = year.astype(str) + "-" +  data["MONTH_ID"].astype(str)
        fig = px.line(data, 
                x="year-month", 
                y="SALES",
                height=350,
                labels={"year-month": "Month-Year",
                        "SALES": "Sales"},
                title="📈 Monthly Sales Trend",
                )
        fig.update_xaxes(type="category")

        return fig
    
    