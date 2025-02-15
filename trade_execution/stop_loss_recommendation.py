class StopLossRecommendation:
    def __init__(self, atr_value, multiplier=1.5):
        self.atr_value = atr_value
        self.multiplier = multiplier

    def recommend_stop_loss(self, entry_price):
        stop_loss = entry_price - (self.atr_value * self.multiplier)
        return round(stop_loss, 4)

# Exemple d'utilisation
stop_recommendation = StopLossRecommendation(atr_value=0.002)
print(stop_recommendation.recommend_stop_loss(entry_price=1.1250))
