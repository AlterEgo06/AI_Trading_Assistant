import yfinance as yf
import pandas as pd

def multi_timeframe(symbol):
    stock = yf.Ticker(symbol)
    data_daily = stock.history(period="6mo")
    data_hourly = stock.history(period="60d", interval="1h")

    if data_daily["Close"].iloc[-1] > data_daily["Close"].rolling(window=20).mean().iloc[-1] and \
       data_hourly["Close"].iloc[-1] > data_hourly["Close"].rolling(window=20).mean().iloc[-1]:
        return "BUY"
    else:
        return "SELL"

if __name__ == "__main__":
    print("Multi-Timeframe Signal EUR/USD :", multi_timeframe("EURUSD=X"))
