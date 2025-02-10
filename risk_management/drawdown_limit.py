class DrawdownLimit:
    def __init__(self, initial_balance, max_drawdown_percent):
        self.initial_balance = initial_balance
        self.max_drawdown = initial_balance * (max_drawdown_percent / 100)
        self.current_balance = initial_balance

    def check_drawdown(self, new_balance):
        self.current_balance = new_balance
        if self.initial_balance - self.current_balance >= self.max_drawdown:
            return "Alerte: Drawdown maximum atteint, arrêtez le trading !"
        return "Drawdown sous contrôle."

# Exemple d'utilisation
dd_limit = DrawdownLimit(initial_balance=10000, max_drawdown_percent=10)
print(dd_limit.check_drawdown(8900))
