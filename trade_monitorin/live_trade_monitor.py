import random
import time

class LiveTradeMonitor:
    def __init__(self, risk_threshold=5):
        self.risk_threshold = risk_threshold

    def check_trade(self, trade):
        if abs(trade["risk_reward"]) < self.risk_threshold:
            return f"Alerte : Trade {trade['pair']} ne respecte pas le ratio risque/rendement !"
        return f"Trade {trade['pair']} sous contrôle."

# Simulation d'utilisation
monitor = LiveTradeMonitor()
while True:
    trade = {"pair": "EUR/USD", "risk_reward": random.uniform(1, 6)}
    print(monitor.check_trade(trade))
    time.sleep(2)  # Simule une analyse toutes les 2 secondes
