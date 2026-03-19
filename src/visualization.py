import matplotlib.pyplot as plt
# from data_loader import loadData 

# sales_data = loadData()

# sales per quaters bar 
def sales_per_quater(df):
    data = df.groupby(["YEAR_ID", "QTR_ID"])["SALES"].sum()
    label = [f"{y}-{q}" for y, q in data.index]
    fig ,ax = plt.subplots()
    ax.bar(label, data.values)
    plt.xticks(rotation=45)
    return fig

# sales per years bar
def sales_per_year(df):
    data = df.groupby("YEAR_ID")["SALES"].sum()
    fig ,ax = plt.subplots()
    ax.bar(data.index, data.values)
    return fig

# sales per product line bar
def sales_per_product(df):
    data = df.groupby("PRODUCTLINE")["SALES"].sum()
    fig ,ax = plt.subplots()
    ax.bar(data.index, data.values)
    return fig

def sales_per_year(df):
    data = df.groupby("YEAR_ID")["SALES"].sum()
    fig ,ax = plt.subplots()
    ax.bar(data.index, data.values)
    return fig
    