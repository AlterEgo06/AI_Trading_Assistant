class StrategySuggestions:
    def __init__(self):
        pass

    def suggest_strategy(self, market_trend, volatility):
        if market_trend == "bullish" and volatility == "low":
            return "📈 Stratégie suggérée : Trend Following avec confirmation RSI."
        elif market_trend == "range" and volatility == "high":
            return "📊 Stratégie suggérée : Mean Reversion avec stop serré."
        return "⚠️ Aucune stratégie claire détectée."

# Exemple d'utilisation
suggestion = StrategySuggestions()
print(suggestion.suggest_strategy(market_trend="bullish", volatility="low"))
