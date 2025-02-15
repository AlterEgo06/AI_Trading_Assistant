class MarketConditions:
    def __init__(self, trend, volatility, volume):
        self.trend = trend
        self.volatility = volatility
        self.volume = volume

    def evaluate_market(self):
        if self.trend == "bullish" and self.volume > 70:
            return "📈 Marché haussier fort. Opportunité d'achat."
        elif self.trend == "bearish" and self.volume > 70:
            return "📉 Marché baissier fort. Opportunité de vente."
        return "⚠️ Pas d'opportunité claire."

# Exemple d'utilisation
market = MarketConditions(trend="bullish", volatility="high", volume=80)
print(market.evaluate_market())
