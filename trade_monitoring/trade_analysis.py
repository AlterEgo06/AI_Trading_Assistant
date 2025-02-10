import json

class TradeAnalysis:
    def __init__(self, log_file="trade_log.json"):
        self.log_file = log_file

    def analyze_trades(self):
        try:
            with open(self.log_file, "r") as file:
                trades = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return "Aucune donnée disponible."

        losing_trades = [trade for trade in trades if trade["profit"] < 0]
        if not losing_trades:
            return "Aucune perte détectée."

        avg_loss = sum(trade["profit"] for trade in losing_trades) / len(losing_trades)
        return {"total_losing_trades": len(losing_trades), "average_loss": round(avg_loss, 2)}

# Exemple d'utilisation
analysis = TradeAnalysis()
print(analysis.analyze_trades())
