import streamlit as st
from stock_service import get_stock_price, plot_stock_price
from prediction import predict_stock_price

st.title("AI Powered Stock Market Prediction")

ticker = st.text_input("Enter Stock Ticker (Example: AAPL)")

if st.button("Get Price"):
    if ticker:
        st.write(get_stock_price(ticker))

if st.button("Show Graph"):
    if ticker:
        plot_stock_price(ticker)
        st.image("assets/stock.png")

prediction_days = st.number_input("Number of days to predict:", min_value=1, max_value=365, value=30, step=1)

if st.button("Predict Price"):
    if ticker:
        result = predict_stock_price(ticker, prediction_days)
        st.write(result)