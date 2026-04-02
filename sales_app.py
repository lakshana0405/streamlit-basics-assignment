import streamlit as st
import pandas as pd

# Title
st.title("Sales Dashboard")
st.subheader("Filter sales by category")

# Data
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Camera"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Electronics"],
    "Sales": [50000, 30000, 20000, 10000, 25000]
}

df = pd.DataFrame(data)

# Sidebar filter
st.sidebar.title("Filter Options")
category = st.sidebar.selectbox("Select Category", df["Category"].unique())

# Filter logic
filtered_df = df[df["Category"] == category]

# Show table
st.dataframe(filtered_df)

# Chart
st.line_chart(filtered_df["Sales"])