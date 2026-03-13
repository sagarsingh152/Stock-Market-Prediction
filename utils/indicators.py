import yfinance as yf


def calculate_sma(ticker, window):

    data = yf.Ticker(ticker).history(period="1y").Close

    return data.rolling(window).mean().iloc[-1]


def calculate_ema(ticker, window):

    data = yf.Ticker(ticker).history(period="1y").Close

    return data.ewm(span=window).mean().iloc[-1]