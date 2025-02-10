import yfinance as yf
import pandas as pd
import talib

def atr_volatility(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="6mo")

    data["ATR"] = talib.ATR(data["High"], data["Low"], data["Close"], timeperiod=14)

    if data["ATR"].iloc[-1] > data["ATR"].rolling(window=50).mean().iloc[-1]:
        return "HIGH VOLATILITY"
    else:
        return "LOW VOLATILITY"

if __name__ == "__main__":
    print("ATR Volatility EUR/USD :", atr_volatility("EURUSD=X"))
