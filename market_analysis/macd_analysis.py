import pandas as pd

def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    """Calcule l'indicateur MACD"""
    short_ema = data['Close'].ewm(span=short_window, adjust=False).mean()
    long_ema = data['Close'].ewm(span=long_window, adjust=False).mean()
    
    data['MACD'] = short_ema - long_ema
    data['Signal_Line'] = data['MACD'].ewm(span=signal_window, adjust=False).mean()
    
    return data

if __name__ == "__main__":
    df = pd.read_csv("market_data.csv")  # Exemple de fichier de données
    df = calculate_macd(df)
    print(df[['Close', 'MACD', 'Signal_Line']].tail())
