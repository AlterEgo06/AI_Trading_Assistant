import pandas as pd

def detect_double_top_bottom(data):
    """
    Détecte des figures de retournement : Double Top / Double Bottom.

    :param data: DataFrame contenant les prix historiques
    :return: DataFrame avec détection des patterns
    """
    data['Highs'] = data['Close'].rolling(window=5).max()
    data['Lows'] = data['Close'].rolling(window=5).min()
    data['Double_Top'] = (data['Close'] == data['Highs']) & (data['Close'].shift(1) < data['Highs'])
    data['Double_Bottom'] = (data['Close'] == data['Lows']) & (data['Close'].shift(1) > data['Lows'])
    return data

if __name__ == "__main__":
    df = pd.read_csv("sample_data.csv")
    df = detect_double_top_bottom(df)
    print(df[df['Double_Top'] | df['Double_Bottom']])
