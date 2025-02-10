class CapitalAllocation:
    def __init__(self, total_capital, strategies):
        self.total_capital = total_capital
        self.strategies = strategies  # Dictionnaire {nom_stratégie: allocation_pourcentage}

    def allocate(self):
        allocation = {strategy: (self.total_capital * (percent / 100)) for strategy, percent in self.strategies.items()}
        return allocation

# Exemple d'utilisation
allocation = CapitalAllocation(total_capital=10000, strategies={"Scalping": 30, "Swing": 40, "Hedging": 30})
print(allocation.allocate())
