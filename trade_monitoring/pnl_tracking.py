import json

class PnLTracking:
    def __init__(self, log_file="trade_log.json"):
        self.log_file = log_file

    def calculate_pnl(self):
        try:
            with open(self.log_file, "r") as file:
                trades = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return "Aucune donnée disponible."

        total_pnl = sum(trade["profit"] for trade in trades)
        return {"total_pnl": total_pnl}

# Exemple d'utilisation
pnl_tracker = PnLTracking()
print(pnl_tracker.calculate_pnl())
