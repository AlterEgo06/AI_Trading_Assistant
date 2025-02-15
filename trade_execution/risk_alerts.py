class RiskAlerts:
    def __init__(self, max_risk_percentage):
        self.max_risk_percentage = max_risk_percentage

    def check_risk(self, current_risk):
        if current_risk > self.max_risk_percentage:
            return "⚠️ Alerte : Risque trop élevé sur ce trade !"
        return "✅ Risque sous contrôle."

# Exemple d'utilisation
alert = RiskAlerts(max_risk_percentage=5)
print(alert.check_risk(current_risk=6))
