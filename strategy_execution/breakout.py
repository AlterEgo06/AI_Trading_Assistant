import yfinance as yf
import pandas as pd

def breakout_strategy(symbol, period=50):
    stock = yf.Ticker(symbol)
    data = stock.history(period="6mo")

    data["High_Max"] = data["High"].rolling(window=period).max()
    data["Low_Min"] = data["Low"].rolling(window=period).min()

    if data["Close"].iloc[-1] > data["High_Max"].iloc[-2]:
        return "BUY"
    elif data["Close"].iloc[-1] < data["Low_Min"].iloc[-2]:
        return "SELL"
    else:
        return "HOLD"

if __name__ == "__main__":
    print("Breakout Signal EUR/USD :", breakout_strategy("EURUSD=X"))
