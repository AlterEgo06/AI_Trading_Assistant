class TradingOpportunities:
    def __init__(self, price_action, volume, volatility):
        self.price_action = price_action
        self.volume = volume
        self.volatility = volatility

    def find_opportunities(self):
        if self.price_action == "breakout" and self.volume > 75 and self.volatility == "high":
            return "💡 Opportunité : Breakout confirmé avec volume élevé."
        elif self.price_action == "pullback" and self.volume > 60:
            return "💡 Opportunité : Pullback sur support détecté."
        return "❌ Aucune opportunité détectée."

# Exemple d'utilisation
opportunities = TradingOpportunities(price_action="breakout", volume=80, volatility="high")
print(opportunities.find_opportunities())
