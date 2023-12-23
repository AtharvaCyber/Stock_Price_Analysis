import yfinance as yf
import streamlit as st

st.title("Stock Price Analysis")

st.write("""
## Explore Google Stock Data

This app displays the historical closing prices and volumes of Google's stock.
""")

# Specify the ticker symbol
symbol = 'GOOGL'

# Fetch data for the specified stock
stock_data = yf.Ticker(symbol).history(period='1d', start='2010-5-31', end='2020-5-31')

# Display closing prices chart
st.write("### Closing Prices Over Time")
st.line_chart(stock_data['Close'])

# Display volume chart
st.write("### Volume Over Time")
st.line_chart(stock_data['Volume'])
