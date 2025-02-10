import yfinance as yf
import pandas as pd

def get_market_data(asset, timeframe="1h", period="7d"):
    """
    Récupère les données de marché pour un actif donné avec le timeframe spécifié.
    
    :param asset: Symbole de l'actif (ex: 'EURUSD=X' pour le Forex)
    :param timeframe: Unité de temps (ex: '1m', '5m', '1h', '1d')
    :param period: Période d'historique à récupérer (ex: '7d', '30d')
    :return: DataFrame contenant les prix historiques
    """
    data = yf.download(asset, period=period, interval=timeframe)
    return data

if __name__ == "__main__":
    asset = "EURUSD=X"
    timeframe = "1h"
    data = get_market_data(asset, timeframe)
    print(data.tail())
