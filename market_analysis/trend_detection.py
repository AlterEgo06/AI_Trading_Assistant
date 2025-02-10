import pandas as pd

def detect_trend(data, short_window=20, long_window=50):
    """
    Détecte la tendance en comparant une moyenne mobile courte et une longue.

    :param data: DataFrame contenant les prix historiques
    :param short_window: Période de la courte moyenne mobile
    :param long_window: Période de la longue moyenne mobile
    :return: DataFrame avec la tendance détectée
    """
    data['Short_MA'] = data['Close'].rolling(window=short_window).mean()
    data['Long_MA'] = data['Close'].rolling(window=long_window).mean()
    data['Trend'] = data['Short_MA'] > data['Long_MA']
    return data

if __name__ == "__main__":
    df = pd.read_csv("sample_data.csv")
    df = detect_trend(df)
    print(df.tail())
