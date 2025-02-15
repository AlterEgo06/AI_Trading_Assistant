class TradingSignals:
    def __init__(self):
        pass

    def generate_signal(self, rsi, macd, trend):
        if rsi < 30 and macd > 0 and trend == "bullish":
            return "🟢 Signal d'achat détecté."
        elif rsi > 70 and macd < 0 and trend == "bearish":
            return "🔴 Signal de vente détecté."
        return "⚠️ Pas de signal clair."

# Exemple d'utilisation
signals = TradingSignals()
print(signals.generate_signal(rsi=28, macd=1.2, trend="bullish"))
