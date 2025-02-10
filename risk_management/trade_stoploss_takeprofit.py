class TradeStopLossTakeProfit:
    def __init__(self, entry_price, risk_reward_ratio, stop_loss_pips):
        self.entry_price = entry_price
        self.risk_reward_ratio = risk_reward_ratio
        self.stop_loss_pips = stop_loss_pips

    def calculate_levels(self):
        stop_loss = self.entry_price - self.stop_loss_pips
        take_profit = self.entry_price + (self.stop_loss_pips * self.risk_reward_ratio)
        return {"stop_loss": stop_loss, "take_profit": take_profit}

# Exemple d'utilisation
trade = TradeStopLossTakeProfit(entry_price=100, risk_reward_ratio=2, stop_loss_pips=5)
print(trade.calculate_levels())
