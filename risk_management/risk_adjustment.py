class RiskAdjustment:
    def __init__(self, initial_risk, performance):
        self.initial_risk = initial_risk
        self.performance = performance  # Gains/pertes en %

    def adjust_risk(self):
        if self.performance > 5:
            return self.initial_risk * 1.2  # Augmente le risque
        elif self.performance < -5:
            return self.initial_risk * 0.8  # Réduit le risque
        return self.initial_risk

# Exemple d'utilisation
risk = RiskAdjustment(initial_risk=0.02, performance=-6)
print("Nouveau risque par trade :", risk.adjust_risk())
