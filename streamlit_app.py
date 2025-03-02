import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Page title
st.title("Stock Data Dashboard 📈")

# Sidebar inputs
st.sidebar.header("BA870-AC820 StreamLit Example")
ticker_symbol = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, MSFT)", value="MSFT")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2024-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2024-12-31"))

# Fetching data
st.write(f"Fetching data for **{ticker_symbol}** from {start_date} to {end_date}...")
data = yf.download(ticker_symbol, start=start_date, end=end_date)

if data.empty:
    st.error("No data found. Please check the ticker symbol or date range.")
    st.stop()

# Initialize Tabs
tabs = st.tabs(["📋 Raw Data", "📈 Price Chart", "📊 Volume Chart"])

# Tab 1: Raw Data
with tabs[0]:
    st.subheader(f"Raw Data for {ticker_symbol}")
    st.dataframe(data, use_container_width=True)

# Tab 2: Closing Price Chart
with tabs[1]:
    if "Close" in data:
        st.subheader("Closing Price Over Time")
        st.line_chart(data['Close'])
    else:
        st.warning("Closing price data is not available for this stock.")

# Tab 3: Volume Chart
with tabs[2]:
    if "Volume" in data:
        st.subheader("Volume Over Time")
        st.bar_chart(data['Volume'])
    else:
        st.warning("Volume data is not available for this stock.")
        
