import yfinance as yf
import pandas as pd

def pivot_points(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="6mo")

    data["Pivot"] = (data["High"].shift(1) + data["Low"].shift(1) + data["Close"].shift(1)) / 3
    data["R1"] = (2 * data["Pivot"]) - data["Low"].shift(1)
    data["S1"] = (2 * data["Pivot"]) - data["High"].shift(1)

    if data["Close"].iloc[-1] > data["R1"].iloc[-1]:
        return "BUY"
    elif data["Close"].iloc[-1] < data["S1"].iloc[-1]:
        return "SELL"
    else:
        return "HOLD"

if __name__ == "__main__":
    print("Pivot Points Signal EUR/USD :", pivot_points("EURUSD=X"))
