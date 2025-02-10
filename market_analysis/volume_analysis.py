import pandas as pd

def analyze_volume(data):
    """
    Analyse les volumes pour détecter des anomalies dans le marché.

    :param data: DataFrame contenant les prix et les volumes
    :return: DataFrame avec l'analyse des volumes
    """
    data['Avg_Volume'] = data['Volume'].rolling(window=20).mean()
    data['Volume_Surge'] = data['Volume'] > (data['Avg_Volume'] * 1.5)
    return data

if __name__ == "__main__":
    df = pd.read_csv("sample_data.csv")
    df = analyze_volume(df)
    print(df[df['Volume_Surge']])
