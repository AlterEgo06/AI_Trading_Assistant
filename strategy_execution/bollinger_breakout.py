import yfinance as yf
import pandas as pd

def bollinger_breakout(symbol, period=20):
    stock = yf.Ticker(symbol)
    data = stock.history(period="3mo")

    data["SMA"] = data["Close"].rolling(window=period).mean()
    data["Upper"] = data["SMA"] + (data["Close"].rolling(window=period).std() * 2)
    data["Lower"] = data["SMA"] - (data["Close"].rolling(window=period).std() * 2)

    if data["Close"].iloc[-1] > data["Upper"].iloc[-1]:
        return "BUY"
    elif data["Close"].iloc[-1] < data["Lower"].iloc[-1]:
        return "SELL"
    else:
        return "HOLD"

if __name__ == "__main__":
    print("Signal Bollinger Bands EUR/USD :", bollinger_breakout("EURUSD=X"))
