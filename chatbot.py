from stock_service import get_stock_price
from prediction import predict_stock_price


def chatbot():

    print("StockBot Ready")

    while True:

        user = input("You: ").lower()

        if user in ["exit","quit"]:
            break

        if "price" in user:
            ticker = input("Ticker: ")
            print(get_stock_price(ticker))

        elif "predict" in user:
            ticker = input("Ticker: ")
            print(predict_stock_price(ticker))

        else:
            print("Ask about stock price or prediction")