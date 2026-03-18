# Business Sales Data Analysis Dashboard

## Project Overview

This project analyzes a sales dataset to understand business performance across different dimensions such as **product line, country, month, quarter, and year**.

The data was cleaned using Python and visualized using charts to identify key trends and insights.

## Business Questions Answered

This analysis aims to answer the following business questions:

1. Which countries generate the highest sales?
2. Which product lines are the most profitable?
3. How do sales change across months and quarters?
4. Is there any seasonal trend in sales?
5. Which year had the highest sales growth?

## Project Structure

```
data/
 ├── raw/
 │   └── sales_data_sample.csv
 └── processed/
     └── clean_sales_data.csv

notebooks/
 └── 01_explore.ipynb

scripts/
 ├── 01_cleaning.py
 └── 02_visualization.py

reports/
 ├── figures/
 └── summary.txt

requirements.txt
README.md
```

## Technologies Used

* Python
* Pandas
* Matplotlib
* Jupyter Notebook
* VS Code

## Data Cleaning Steps

The following preprocessing steps were performed:

* Converted ORDERDATE to datetime format
* Removed duplicate rows
* Checked for missing values
* Aggregated sales data for visualization

The cleaned dataset was stored in:

data/processed/clean_sales_data.csv

## Visualizations Created

The following charts were generated:

1. Sales by Country (Bar Chart)
2. Sales by Month (Line Chart)
3. Sales by Product Line (Bar Chart)
4. Sales by Quarter (Bar Chart)
5. Sales by Year (Bar Chart)
6. Monthly Sales Trend (Heat map)
7. Sales by Product Line (pie Chart)

These charts help identify business performance trends and seasonal patterns.

## Key Insights

* Certain countries contribute significantly higher sales.
* Sales show seasonal trends across months.
* Some product lines generate more revenue than others.

## How to Run the Project

1. Clone the repository
2. Install dependencies

```
pip install -r requirements.txt
```

3. Run data cleaning

```
python scripts/01_cleaning.py
```

4. Run visualization

```
python scripts/02_visualization.py
```

## Author
Avaneesh singh

Data Analysis Project built using Python.
