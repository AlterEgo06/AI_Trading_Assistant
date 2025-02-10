class RiskHedging:
    def __init__(self, primary_asset, correlated_asset, hedge_ratio):
        self.primary_asset = primary_asset
        self.correlated_asset = correlated_asset
        self.hedge_ratio = hedge_ratio

    def hedge_trade(self, primary_position):
        hedge_position = -primary_position * self.hedge_ratio
        return hedge_position

# Exemple d'utilisation
hedging = RiskHedging(primary_asset="EUR/USD", correlated_asset="USD/CHF", hedge_ratio=0.8)
print("Position de couverture :", hedging.hedge_trade(1))
