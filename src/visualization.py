import pandas as pd
import plotly.express as px

# apply filter
def apply_filter(df: pd.DataFrame, year , country : str , product: str):
        df_filter = df.copy()
        if year != "All":
                df_filter = df_filter[df_filter["YEAR_ID"] == year]

        if product != "All":
                df_filter = df_filter[df_filter["PRODUCTLINE"] == product]
                
        if country != "All":
                df_filter = df_filter[df_filter["COUNTRY"] == country]
                
        return df_filter

# sales per quaters bar 
def sales_per_quarter(df: pd.DataFrame, year,country: str  , product: str):
         
        df_filter = apply_filter(df, year, country, product)
        
                        
        data = (df_filter.groupby(["YEAR_ID", "QTR_ID"])["SALES"]
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

# sales per years bar
def sales_per_year(df: pd.DataFrame, country: str  , product: str):
        year = "All"
        df_filter = apply_filter(df, year, country, product)
        
        
        data = (df_filter.groupby("YEAR_ID")["SALES"]
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
        
        product = "All"
        
        df_filter = apply_filter(df, year, country, product)
       
        data = (df_filter
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
                title=f"📊 Sales by Product Line in {"All country" if country == "All" else country}"
                )
        return fig
    
# sales per country
def sales_per_country(df: pd.DataFrame, year,country: str  , product: str):
        highlighted_country = country
        country = "All"
        df_filter = apply_filter(df, year, country, product)
        
        data = (df_filter
                .groupby("COUNTRY")["SALES"]
                .sum()
                .sort_values()
                .reset_index()
                )
        
        
        data["COLOR"] = data["COUNTRY"].apply(lambda c: highlighted_country if c == highlighted_country else "Other")
        fig = px.bar(data, 
                        x="SALES",
                        y="COUNTRY",
                        color="COLOR",
                        color_discrete_map={f"{highlighted_country}": "green", "Other": "skyblue"},
                        height=500,
                        width=500,
                        orientation="h",
                        labels={"COUNTRY": "Countrys", "SALES": "Sales"},
                        title="🌍 Sales by Country",
                        )
        return fig

# sales per month
def sales_per_month(df: pd.DataFrame, year,country: str  , product: str):
        df_filter = apply_filter(df, year, country, product)
    
        data = (df_filter
                .groupby(["YEAR_ID", "MONTH_ID"])["SALES"]
                .sum()
                .reset_index()
                )
        
        data["year-month"] = data["YEAR_ID"].astype(str) + "-" +  data["MONTH_ID"].astype(str)
        fig = px.line(data, 
                x="year-month", 
                y="SALES",
                height=350,
                labels={"year-month": "Year-Month",
                        "SALES": "Sales"},
                title="📈 Monthly Sales Trend",
                )
        fig.update_xaxes(type="category")

        return fig
    
    