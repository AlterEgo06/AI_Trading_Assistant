import requests

def get_sentiment_analysis(keyword="stock market"):
    """
    Analyse le sentiment du marché en récupérant des nouvelles financières.

    :param keyword: Terme de recherche pour l'analyse du sentiment
    :return: Score de sentiment basé sur l'actualité
    """
    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey=TON_API_KEY"
    response = requests.get(url).json()
    
    sentiment_score = 0
    for article in response['articles']:
        if "bullish" in article['title'].lower():
            sentiment_score += 1
        elif "bearish" in article['title'].lower():
            sentiment_score -= 1
    
    return sentiment_score

if __name__ == "__main__":
    sentiment = get_sentiment_analysis()
    print(f"Sentiment Score: {sentiment}")
