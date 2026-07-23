📊 Retail Sales Analytics Dashboard

An end-to-end Retail Sales Analytics project built using **Python, SQL, Pandas, Plotly, and Streamlit**. The project demonstrates the complete data analytics workflow—from data cleaning and exploratory analysis to SQL querying and deployment of an interactive business intelligence dashboard.

📌 Project Overview

This project analyzes the **Sample Superstore Dataset** to uncover business insights related to sales, profitability, customer behavior, and regional performance.

The project follows a complete analytics pipeline:

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- SQL Analysis
- Interactive Dashboard Development
- Business Insight Generation

🚀 Dashboard Features

📈 Interactive Filters
- Year
- Region
- Product Category
- Customer Segment

📊 KPI Cards
- Total Revenue
- Total Profit
- Total Orders
- Total Customers
- Profit Margin
- Year-over-Year Growth

📉 Visualizations

- Monthly Sales Trend
- Sales by Category
- Sales by Region
- Top 10 Product Sub-Categories
- Top Customers by Revenue
- Regional Profit Analysis
- Profit Distribution by Discount

💡 Dynamic Business Insights

The dashboard automatically identifies:

- Highest Revenue Category
- Best Performing Region
- Largest Customer Segment
- Most Profitable Product Category
- Highest Value Customer
- Discount Impact on Profitability

📥 Export Feature

Users can download the filtered dataset directly as a CSV file.


📂 Project Structure


sales-analysis-project/
│
├── app/
│   └── app.py                 # Streamlit Dashboard
│
├── data/
│   └── superstore.csv         # Dataset
│
├── notebooks/
│   └── analysis.ipynb         # EDA Notebook
│
│
├── outputs/
│   └── Dashboard            # Dashboard Sample Images
│
├── visuals/
│   └── EDA                  # EDA Visualizations
│   └── Querying             # Querying Visualizations
│
├── README.md
└── requirements.txt



🛠️ Technologies Used

Programming

- Python

Libraries

- Pandas
- NumPy
- Plotly Express
- Streamlit
- Matplotlib
- Seaborn

Database

- SQLite
- SQL

Development Tools

- Jupyter Notebook
- VS Code
- Git
- GitHub

📈 Analytical Workflow

1️⃣ Data Cleaning

- Removed duplicate records
- Checked missing values
- Converted date columns
- Feature engineering
  - Year
  - Month
  - Profit Margin


2️⃣ Exploratory Data Analysis

Performed exploratory analysis to understand:

- Sales trends
- Profit distribution
- Customer behavior
- Regional performance
- Product performance
- Discount impact


3️⃣ SQL Analysis

Used SQL to answer business questions including:

- Total Revenue
- Highest Selling Categories
- Top Customers
- Regional Performance
- Profitability Analysis
- Discount Analysis

4️⃣ Dashboard Development

Developed an interactive Streamlit dashboard with:

- Responsive Layout
- Dynamic Filters
- Plotly Interactive Charts
- KPI Cards
- Downloadable Reports
- Business Insights

📊 Key Business Insights

The dashboard dynamically generates insights such as:

- Technology products consistently generate strong revenue.
- The West region contributes the highest sales in multiple years.
- Higher discounts generally reduce profitability.
- Consumer customers place the highest number of orders.
- A small number of customers contribute disproportionately to total revenue.

📷 Dashboard Preview

Executive Dashboard

- KPI Cards
- Monthly Sales Trend
- Interactive Filters

Sales Analysis

- Category Performance
- Regional Sales
- Regional Profit

Customer Analysis

- Top Customers
- Top Products
- Discount vs Profit


▶️ Running the Project

Clone Repository

```bash
git clone https://github.com/yourusername/retail-sales-dashboard.git
```


Install Requirements

```bash
pip install -r requirements.txt
```

Launch Dashboard

```bash
streamlit run app/app.py
```

📌 Future Improvements

- Forecasting using Time Series Models
- Customer Segmentation (RFM Analysis)
- Sales Prediction
- Inventory Analytics
- Geographic Sales Maps
- Power BI Version
- Docker Deployment
- Cloud Deployment (Streamlit Community Cloud)

⭐ Project Highlights

✔ End-to-End Data Analytics Project

✔ SQL + Python Integration

✔ Interactive Streamlit Dashboard

✔ Dynamic Business Insights

✔ Downloadable Reports

✔ Recruiter-Friendly Portfolio Project
