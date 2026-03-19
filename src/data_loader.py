import pandas as pd
import os

def loadData():
    sales_data = pd.read_csv(os.path.join("data/processed/clean_sales_data.csv"))
    return sales_data
