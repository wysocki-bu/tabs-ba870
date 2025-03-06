# Import necessary packages (* Make sure to also include in "requirements.txt" in this repository
import streamlit as st
import yfinance as yf
import pandas as pd

# Print Title for the App
st.title("Stock Data Dashboard Using **yfinance** Package")

# Create a Sidebar which prompts for stock ticker and dates
st.sidebar.header("BA870-AC820 StreamLit Example")
ticker_symbol = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, MSFT)", value="MSFT")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2024-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2024-12-31"))

# Update the name of ticker anbd dates and download data using yfinace "download" function
st.write(f"Data for **{ticker_symbol}** from {start_date} to {end_date}:")
data = yf.download(ticker_symbol, start=start_date, end=end_date)

if data.empty:
    st.error("No data available. Check the ticker symbol or date range.")
    st.stop()

# Set up the 3 tabs on the Dashboard
tabs = st.tabs(["📋 Raw Data", "📈 Price Chart", "📊 Volume Chart"])

# Tab 1: Raw Data
with tabs[0]:
    st.subheader(f"Raw Data for {ticker_symbol}")
    st.dataframe(data, use_container_width=True)

# Tab 2: Closing Price Chart
with tabs[1]:
    if "Close" in data:
        st.subheader(f"Closing Price for {ticker_symbol}")
        st.line_chart(data['Close'])
    else:
        st.warning(f"Closing price data is not available for ticker symbol: {ticker_symbol}.")

# Tab 3: Volume Chart
with tabs[2]:
    if "Volume" in data:
        st.subheader(f"Volume for {ticker_symbol}")
        st.bar_chart(data['Volume'])
    else:
        st.warning("Volume data is not available for ticker symbol: {ticker_symbol}.")
        
