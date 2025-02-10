import yfinance as yf
import pandas as pd

def ema_crossover(symbol, short_window=9, long_window=21):
    stock = yf.Ticker(symbol)
    data = stock.history(period="3mo")
    
    data["ShortEMA"] = data["Close"].ewm(span=short_window, adjust=False).mean()
    data["LongEMA"] = data["Close"].ewm(span=long_window, adjust=False).mean()

    if data["ShortEMA"].iloc[-1] > data["LongEMA"].iloc[-1]:
        return "BUY"
    else:
        return "SELL"

if __name__ == "__main__":
    print("Signal EMA EUR/USD :", ema_crossover("EURUSD=X"))
