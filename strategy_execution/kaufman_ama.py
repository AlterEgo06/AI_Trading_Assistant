import yfinance as yf
import pandas as pd
import talib

def kaufman_ama(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="6mo")

    data["AMA"] = talib.EMA(data["Close"], timeperiod=14)

    if data["Close"].iloc[-1] > data["AMA"].iloc[-1]:
        return "BUY"
    elif data["Close"].iloc[-1] < data["AMA"].iloc[-1]:
        return "SELL"
    else:
        return "HOLD"

if __name__ == "__main__":
    print("Kaufman AMA Signal EUR/USD :", kaufman_ama("EURUSD=X"))
