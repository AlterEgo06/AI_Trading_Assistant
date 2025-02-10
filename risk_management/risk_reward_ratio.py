class RiskRewardRatio:
    def __init__(self, entry_price, stop_loss_price, take_profit_price):
        self.entry_price = entry_price
        self.stop_loss_price = stop_loss_price
        self.take_profit_price = take_profit_price

    def calculate_ratio(self):
        risk = abs(self.entry_price - self.stop_loss_price)
        reward = abs(self.take_profit_price - self.entry_price)
        if risk == 0:
            return "Erreur: Stop loss mal défini."
        return round(reward / risk, 2)

# Exemple d'utilisation
rr = RiskRewardRatio(entry_price=100, stop_loss_price=95, take_profit_price=110)
print("Risk-Reward Ratio:", rr.calculate_ratio())
