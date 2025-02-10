import pandas as pd
import numpy as np
import yfinance as yf
import json

def load_assets(file="config.json"):
    with open(file, "r") as f:
        config = json.load(f)
    return config["assets"]

def get_volatility(assets, period="6mo"):
    vol_data = {}
    for asset in assets:
        df = yf.download(asset, period=period)["Close"]
        returns = df.pct_change().dropna()
        vol_data[asset] = np.std(returns) * np.sqrt(252)
    
    return vol_data

if __name__ == "__main__":
    assets = load_assets()
    volatility = get_volatility(assets)
    print(volatility)
