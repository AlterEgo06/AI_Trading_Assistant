import json
import matplotlib.pyplot as plt

class EquityCurve:
    def __init__(self, log_file="trade_log.json"):
        self.log_file = log_file

    def plot_curve(self):
        try:
            with open(self.log_file, "r") as file:
                trades = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return "Aucune donnée disponible."

        balances = [10000]  # Solde initial
        for trade in trades:
            balances.append(balances[-1] + trade["profit"])

        plt.plot(balances, marker="o", linestyle="-", color="b")
        plt.xlabel("Nombre de Trades")
        plt.ylabel("Solde du compte")
        plt.title("Courbe d’Équité")
        plt.show()

# Exemple d'utilisation
equity = EquityCurve()
equity.plot_curve()
