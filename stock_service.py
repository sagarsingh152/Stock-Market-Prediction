import yfinance as yf
import matplotlib.pyplot as plt


def get_stock_price(ticker):
    try:
        ticker = ticker.upper()
        data = yf.Ticker(ticker).history(period="1d")

        if data.empty:
            return "Invalid ticker."

        price = data.Close.iloc[-1]
        return f"Latest price of {ticker}: ${price:.2f}"

    except Exception as e:
        return str(e)


def plot_stock_price(ticker):

    ticker = ticker.upper()
    data = yf.Ticker(ticker).history(period="1y")

    plt.figure(figsize=(10,5))
    plt.plot(data.index, data.Close)

    plt.title(f"{ticker} Stock Price (1 Year)")
    plt.xlabel("Date")
    plt.ylabel("Price")

    plt.grid(True)
    plt.savefig("assets/stock.png")
    plt.close()