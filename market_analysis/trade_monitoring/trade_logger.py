import json
from datetime import datetime

class TradeLogger:
    def __init__(self, log_file="trade_log.json"):
        self.log_file = log_file

    def log_trade(self, trade_details):
        trade_details["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open(self.log_file, "r") as file:
                trades = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            trades = []

        trades.append(trade_details)

        with open(self.log_file, "w") as file:
            json.dump(trades, file, indent=4)

# Exemple d'utilisation
logger = TradeLogger()
logger.log_trade({"pair": "EUR/USD", "entry": 1.1234, "exit": 1.1250, "profit": 16, "risk_reward": 2})
