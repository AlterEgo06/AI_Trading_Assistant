import json

class TradePerformance:
    def __init__(self, log_file="trade_log.json"):
        self.log_file = log_file

    def analyze_performance(self):
        try:
            with open(self.log_file, "r") as file:
                trades = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return "Aucune donnée disponible."

        total_trades = len(trades)
        wins = sum(1 for trade in trades if trade["profit"] > 0)
        losses = total_trades - wins
        win_rate = round((wins / total_trades) * 100, 2) if total_trades > 0 else 0
        avg_risk_reward = round(sum(trade["risk_reward"] for trade in trades) / total_trades, 2) if total_trades > 0 else 0

        return {
            "total_trades": total_trades,
            "win_rate": f"{win_rate}%",
            "average_risk_reward": avg_risk_reward
        }

# Exemple d'utilisation
performance = TradePerformance()
print(performance.analyze_performance())
