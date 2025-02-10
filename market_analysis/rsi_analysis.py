import pandas as pd

def calculate_rsi(data, period=14):
    """Calcule l'indice de force relative (RSI)"""
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    
    return rsi

if __name__ == "__main__":
    df = pd.read_csv("market_data.csv")  # Exemple de fichier de données
    df['RSI'] = calculate_rsi(df)
    print(df[['Close', 'RSI']].tail())
