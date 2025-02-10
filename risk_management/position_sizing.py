class PositionSizing:
    def __init__(self, account_balance, risk_per_trade, stop_loss_pips, pip_value):
        self.account_balance = account_balance
        self.risk_per_trade = risk_per_trade  # En pourcentage (ex: 1% = 0.01)
        self.stop_loss_pips = stop_loss_pips
        self.pip_value = pip_value  # Valeur d'un pip pour l'actif

    def calculate_lot_size(self):
        risk_amount = self.account_balance * self.risk_per_trade
        lot_size = risk_amount / (self.stop_loss_pips * self.pip_value)
        return round(lot_size, 2)

# Exemple d'utilisation
sizing = PositionSizing(account_balance=10000, risk_per_trade=0.02, stop_loss_pips=20, pip_value=10)
print("Lot Size conseillé :", sizing.calculate_lot_size())
