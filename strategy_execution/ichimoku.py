import yfinance as yf
import pandas as pd
import talib

def ichimoku_strategy(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="6mo")

    high9 = data["High"].rolling(window=9).max()
    low9 = data["Low"].rolling(window=9).min()
    data["Tenkan"] = (high9 + low9) / 2

    high26 = data["High"].rolling(window=26).max()
    low26 = data["Low"].rolling(window=26).min()
    data["Kijun"] = (high26 + low26) / 2

    if data["Close"].iloc[-1] > data["Tenkan"].iloc[-1] and data["Tenkan"].iloc[-1] > data["Kijun"].iloc[-1]:
        return "BUY"
    elif data["Close"].iloc[-1] < data["Tenkan"].iloc[-1] and data["Tenkan"].iloc[-1] < data["Kijun"].iloc[-1]:
        return "SELL"
    else:
        return "HOLD"

if __name__ == "__main__":
    print("Ichimoku Signal EUR/USD :", ichimoku_strategy("EURUSD=X"))
