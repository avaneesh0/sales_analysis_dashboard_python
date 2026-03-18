import matplotlib.pyplot as plt
import pandas as pd
import os

sales_data = pd.read_csv(os.path.join("data/processed/clean_sales_data_sample.csv"))

# sales per years bar
sales_data.groupby("YEAR_ID")["SALES"].sum().plot(kind="bar")
plt.title("sales per years")
plt.ylabel("Million $")
plt.xlabel("Year")
plt.xticks(rotation= 45)
plt.savefig("reports/figures/sales_by_Years_bar.png", bbox_inches="tight" )
plt.close()

# sales per quaters bar 
sales_data.groupby(["YEAR_ID", "QTR_ID"])["SALES"].sum().plot(kind="bar")
plt.title("sales per Quater")
plt.ylabel("Million $")
plt.xlabel("Year , Quater")
plt.xticks(rotation= 45)
plt.savefig("reports/figures/sales_by_Quaters_bar.png" , bbox_inches="tight")
plt.close()

# sales per product line bar
sales_data.groupby("PRODUCTLINE")["SALES"].sum().sort_values().plot(kind="bar")
plt.title("sales per product")
plt.ylabel("Million $")
plt.xlabel("Product")
plt.xticks(rotation= 45)
plt.savefig("reports/figures/sales_by_Product_bar", bbox_inches="tight")
plt.close()

# sales per country bar
sales_data.groupby("COUNTRY")["SALES"].sum().sort_values().plot(kind="bar")
plt.title("sales per Country")
plt.ylabel("Million $")
plt.xlabel("Country")
plt.xticks(rotation= 45)
plt.savefig("reports/figures/sales_by_Country_bar", bbox_inches="tight")
plt.close()

# sales per month line
grouped = sales_data.groupby(["YEAR_ID", "MONTH_ID"])["SALES"].sum()
x = [f"{y}-{m}" for y, m in grouped.index]
grouped.plot(kind="line",  figsize=[13, 6])
plt.xticks(range(len(x)), x, rotation= 45)
plt.title("sales over a period of time")
plt.ylabel("Million $")
plt.xlabel("date")
plt.savefig("reports/figures/sales_by_month_line.png", bbox_inches="tight")
plt.close()

# sales per product pie
sales_data.groupby("PRODUCTLINE")["SALES"].sum().sort_values(ascending=False).plot(
    kind="pie", 
    autopct='%1.1f%%', 
    startangle=90, 
    pctdistance=0.85 , 
)
plt.title("Sales per Product Line")
plt.savefig("reports/figures/sales_by_product_pie.png", bbox_inches="tight")
plt.close()

# sales by year and month heatmap
grouped = sales_data.groupby(["YEAR_ID", "MONTH_ID"])["SALES"].sum().reset_index()
pivot = grouped.pivot(index="MONTH_ID", columns="YEAR_ID", values="SALES")
plt.figure(figsize=(10, 6))
plt.imshow(pivot, cmap='viridis', aspect='auto')
plt.colorbar(label='Sales (Million $)')
plt.xticks(range(len(pivot.columns)), pivot.columns )
plt.yticks(range(len(pivot.index)), pivot.index)
plt.xlabel('Year')
plt.ylabel('Month')
plt.title('Sales Heatmap by Year and Month')
plt.savefig("reports/figures/sales_by_Month_Heatmap.png", bbox_inches="tight")
plt.close()