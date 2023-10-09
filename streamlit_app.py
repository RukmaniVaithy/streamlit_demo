import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Create dummy stock data
def create_dummy_data():
    np.random.seed(0)
    days = pd.date_range(start="2022-01-01", end="2022-12-31", freq="D")
    stocks = ["AAPL", "GOOGL", "TSLA", "MSFT"]
    data = {
        "Date": np.random.choice(days, size=100),
        "Stock": np.random.choice(stocks, size=100),
        "Price": np.random.uniform(100, 300, size=100),
    }
    return pd.DataFrame(data)

stock_data = create_dummy_data()

# Streamlit app
st.title("Stock Data Explorer")

# Filter by stock
selected_stock = st.selectbox("Select Stock", stock_data["Stock"].unique())

filtered_data = stock_data[stock_data["Stock"] == selected_stock]

# Display filtered data
st.write(f"Displaying data for {selected_stock}")
st.write(filtered_data)

# Interactive visualizations
st.subheader("Interactive Visualizations")
visualization_choice = st.selectbox("Select Visualization Type", ["Line Chart", "Bar Chart"])

if visualization_choice == "Line Chart":
    # Line Chart
    fig = px.line(filtered_data, x="Date", y="Price", title=f"Stock Prices for {selected_stock}")
    st.plotly_chart(fig)

elif visualization_choice == "Bar Chart":
    # Bar Chart
    fig = px.bar(filtered_data, x="Date", y="Price", title=f"Stock Prices for {selected_stock}")
    st.plotly_chart(fig)
