import yfinance as yf
import numpy as np
from sklearn.linear_model import LinearRegression


def predict_stock_price(ticker, days=30):

    ticker = ticker.upper()

    data = yf.Ticker(ticker).history(period="1y").Close

    X = np.arange(len(data)).reshape(-1,1)
    y = data.values

    model = LinearRegression()
    model.fit(X,y)

    future = np.arange(len(data), len(data)+days).reshape(-1,1)

    prediction = model.predict(future)

    return f"Predicted price after {days} days: ${prediction[-1]:.2f}"