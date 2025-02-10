import pandas as pd
import yfinance as yf
import json

# Charger la liste des actifs depuis un fichier JSON
def load_assets(file="config.json"):
    with open(file, "r") as f:
        config = json.load(f)
    return config["assets"]

def get_correlation(assets, period="6mo"):
    data = {asset: yf.download(asset, period=period)["Close"] for asset in assets}
    df = pd.DataFrame(data)
    return df.corr()

if __name__ == "__main__":
    assets = load_assets()
    correlation = get_correlation(assets)
    print(correlation)
