class ExecutionMonitor:
    def __init__(self):
        self.trade_history = []

    def log_trade(self, trade_details):
        self.trade_history.append(trade_details)

    def analyze_performance(self):
        total_trades = len(self.trade_history)
        wins = sum(1 for trade in self.trade_history if trade["profit"] > 0)
        win_rate = (wins / total_trades) * 100 if total_trades > 0 else 0
        return {"total_trades": total_trades, "win_rate": f"{win_rate:.2f}%"}

# Exemple d'utilisation
monitor = ExecutionMonitor()
monitor.log_trade({"symbol": "EUR/USD", "profit": 10})
monitor.log_trade({"symbol": "GBP/USD", "profit": -5})
print(monitor.analyze_performance())
