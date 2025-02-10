import yfinance as yf
import pandas as pd

def mean_reversion(symbol, period=20):
    stock = yf.Ticker(symbol)
    data = stock.history(period="6mo")

    data["SMA"] = data["Close"].rolling(window=period).mean()

    if data["Close"].iloc[-1] < data["SMA"].iloc[-1] * 0.98:
        return "BUY"
    elif data["Close"].iloc[-1] > data["SMA"].iloc[-1] * 1.02:
        return "SELL"
    else:
        return "HOLD"

if __name__ == "__main__":
    print("Mean Reversion Signal EUR/USD :", mean_reversion("EURUSD=X"))
