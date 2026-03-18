import pandas as pd
import os

sales_data = pd.read_csv(os.path.join(r"data/raw/sales_data_sample.csv"))

sales_data["ORDERDATE"] = pd.to_datetime(sales_data["ORDERDATE"])

# replaced all NaN/null values with the string "Missing"
sales_data["ADDRESSLINE2"] = sales_data["ADDRESSLINE2"].fillna("Missing")
sales_data["STATE"] = sales_data["STATE"].fillna("Missing")
sales_data["POSTALCODE"] = sales_data["POSTALCODE"].fillna("Missing")
sales_data["TERRITORY"] = sales_data["TERRITORY"].fillna("Missing")
sales_data = sales_data[sales_data["STATUS"] == "Shipped"]

# save clean dataset in different file
sales_data.to_csv(os.path.join("data/processed/clean_sales_data_sample.csv"), index=False)