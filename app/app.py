from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px
# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Retail Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# ----------------------------
# Load Dataset
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "superstore.csv"

df = pd.read_csv(DATA_PATH, encoding="latin1")

# ----------------------------
# Convert Date Column
# ----------------------------
df["Order Date"] = pd.to_datetime(df["Order Date"])

# ----------------------------
# Create Extra Columns
# ----------------------------
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month

# ----------------------------
# Dashboard Title
# ----------------------------
st.title("📊 Retail Sales Analytics Dashboard")

st.markdown(
    "Interactive dashboard for exploring sales, profit, customers and regional performance."
)

# ============================
# Sidebar Filters
# ============================

st.sidebar.title("📊 Retail Sales Analytics Dashboard")

st.sidebar.subheader("🎯 Dashboard Filters")

st.sidebar.info(
"""
**Dataset:** Superstore

**Records:** {:,}

**Developer:** Sriravinaa R K
""".format(len(df))
)
years = sorted(df["Year"].unique())

selected_year = st.sidebar.selectbox(
    "Year",
    years
)
regions = sorted(df["Region"].unique())

selected_region = st.sidebar.selectbox(
    "Region",
    ["All"] + regions
)
categories = sorted(df["Category"].unique())

selected_category = st.sidebar.selectbox(
    "Category",
    ["All"] + categories
)
segments = sorted(df["Segment"].unique())

selected_segment = st.sidebar.selectbox(
    "Customer Segment",
    ["All"] + segments
)
filtered_df = df.copy()

filtered_df = filtered_df[
    filtered_df["Year"] == selected_year
]

if selected_region != "All":
    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]

if selected_segment != "All":
    filtered_df = filtered_df[
        filtered_df["Segment"] == selected_segment
    ]

# ============================
# KPI Calculations
# ============================

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
profit_margin = (total_profit / total_sales * 100) if total_sales else 0
total_orders = len(filtered_df)
total_customers = filtered_df["Customer ID"].nunique()
# ============================
# KPI Cards
# ============================

current_year = selected_year

previous_df = df[df["Year"] == current_year - 1]

previous_sales = previous_df["Sales"].sum()
previous_profit = previous_df["Profit"].sum()
previous_orders = len(previous_df)
previous_customers = previous_df["Customer ID"].nunique()

def growth(curr, prev):
    if prev == 0:
        return 0
    return ((curr - prev) / prev) * 100

sales_growth = growth(total_sales, previous_sales)
profit_growth = growth(total_profit, previous_profit)
orders_growth = growth(total_orders, previous_orders)
customer_growth = growth(total_customers, previous_customers)

col1, col2, col3, col4, col5 = st.columns(5)

cards = [
    ("Total Revenue", total_sales, sales_growth, "#00C853"),
    ("Total Profit", total_profit, profit_growth, "#2196F3"),
    ("Orders", total_orders, orders_growth, "#FF9800"),
    ("Customers", total_customers, customer_growth, "#9C27B0"),
    ("Profit Margin", f"{profit_margin:.2f}%", 0, "#00BCD4")
]

for col, (title, value, change, color) in zip([col1,col2,col3,col4], cards):

    symbol = "▲" if change >= 0 else "▼"

    col.markdown(f"""
    <div style="
    background:#232323;
    padding:20px;
    border-radius:15px;
    border-left:6px solid {color};
    box-shadow:0 3px 10px rgba(0,0,0,0.3);
    ">

    <h4>{title}</h4>

    <h2>{value:,.0f}</h2>

    <p style="color:{'#00E676' if change>=0 else '#FF5252'};">
    {symbol} {abs(change):.1f}% vs Previous Year
    </p>

    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.subheader("📈 Monthly Sales Trend")

monthly_sales = (
    filtered_df.assign(
        YearMonth=filtered_df["Order Date"].dt.to_period("M").astype(str)
    )
    .groupby("YearMonth")["Sales"]
    .sum()
    .reset_index()
)

fig_monthly = px.line(
    monthly_sales,
    x="YearMonth",
    y="Sales",
    markers=True,
    title="Monthly Sales"
)

st.plotly_chart(fig_monthly, use_container_width=True)
st.markdown("---")

col1, col2 = st.columns(2)
category_sales = (
    filtered_df
    .groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig1 = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    color="Category",
    title="Sales by Category"
)

col1.plotly_chart(fig1, use_container_width=True)
region_sales = (
    filtered_df
    .groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig_region = px.bar(
    region_sales,
    x="Sales",
    y="Region",
    orientation="h",
    text_auto=".2s",
    color="Sales",
    color_continuous_scale="Blues",
    title="Sales by Region"
)

fig_region.update_layout(
    template="plotly_dark",
    coloraxis_showscale=False
)

col2.plotly_chart(fig_region, use_container_width=True)
st.markdown("---")

col3, col4 = st.columns(2)
top_products = (
    filtered_df
    .groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig3 = px.bar(
    top_products,
    x="Sales",
    y="Sub-Category",
    orientation="h",
    title="Top 10 Products"
)

col3.plotly_chart(fig3, use_container_width=True)
top_customers = (
    filtered_df
    .groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig4 = px.bar(
    top_customers,
    x="Sales",
    y="Customer Name",
    orientation="h",
    title="Top Customers"
)

col4.plotly_chart(fig4, use_container_width=True)
profit_region = (
    filtered_df
    .groupby("Region")["Profit"]
    .sum()
    .reset_index()
)

fig_profit_region = px.bar(
    profit_region,
    x="Region",
    y="Profit",
    color="Profit",
    color_continuous_scale="Greens",
    text_auto=".2s",
    title="Regional Profit"
)

fig_profit_region.update_layout(
    template="plotly_dark",
    coloraxis_showscale=False
)

st.plotly_chart(fig_profit_region,use_container_width=True)

discount_profit = (
    filtered_df
    .groupby("Discount")["Profit"]
    .mean()
    .reset_index()
)
fig_discount = px.box(
    filtered_df,
    x="Discount",
    y="Profit",
    color="Category",
    title="Profit Distribution by Discount"
)

fig_discount.update_layout(
    template="plotly_dark"
)

st.plotly_chart(fig_discount,use_container_width=True)

st.markdown("---")

st.header("📌 Business Insights")

top_category = (
    filtered_df.groupby("Category")["Sales"]
    .sum()
    .idxmax()
)

top_region = (
    filtered_df.groupby("Region")["Sales"]
    .sum()
    .idxmax()
)

top_segment = (
    filtered_df.groupby("Segment")
    .size()
    .idxmax()
)

top_product = (
    filtered_df.groupby("Sub-Category")["Profit"]
    .sum()
    .idxmax()
)

best_customer = (
    filtered_df.groupby("Customer Name")["Sales"]
    .sum()
    .idxmax()
)

avg_discount = filtered_df["Discount"].mean()

discount_msg = (
    "Average discount is high and may reduce profitability."
    if avg_discount > 0.25
    else
    "Current discount strategy appears healthy."
)

st.header("📌 Executive Summary")

st.success(
    f"Highest sales category: **{top_category}**"
)

st.info(
    f"Top revenue region: **{top_region}**"
)

st.warning(
    discount_msg
)

st.success(
    f"Most profitable sub-category: **{top_product}**"
)

st.info(
    f"Highest value customer: **{best_customer}**"
)

st.success(
    f"Largest customer segment: **{top_segment}**"
)

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Filtered Data",
    csv,
    "filtered_sales.csv",
    "text/csv"
)

st.markdown("---")
st.header("Filtered Dataset")

st.dataframe(filtered_df)
st.markdown("---")

st.caption(
"""
Retail Sales Analytics Dashboard

Developed by Sriravinaa R K

Tech Stack:
Python • Pandas • SQL • Plotly • Streamlit

Dataset:
Sample Superstore Dataset

Version 1.0
"""
)

