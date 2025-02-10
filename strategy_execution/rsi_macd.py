import yfinance as yf
import pandas as pd
import talib

def rsi_macd_strategy(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="6mo")

    data["RSI"] = talib.RSI(data["Close"], timeperiod=14)
    macd, macd_signal, _ = talib.MACD(data["Close"], fastperiod=12, slowperiod=26, signalperiod=9)

    if data["RSI"].iloc[-1] < 30 and macd.iloc[-1] > macd_signal.iloc[-1]:
        return "BUY"
    elif data["RSI"].iloc[-1] > 70 and macd.iloc[-1] < macd_signal.iloc[-1]:
        return "SELL"
    else:
        return "HOLD"

if __name__ == "__main__":
    print("Signal RSI + MACD EUR/USD :", rsi_macd_strategy("EURUSD=X"))
