class PositionTracking:
    def __init__(self, initial_entry, trailing_stop_pips):
        self.initial_entry = initial_entry
        self.trailing_stop_pips = trailing_stop_pips
        self.current_stop_loss = initial_entry - trailing_stop_pips

    def update_stop_loss(self, new_high):
        if new_high - self.trailing_stop_pips > self.current_stop_loss:
            self.current_stop_loss = new_high - self.trailing_stop_pips
        return self.current_stop_loss

# Exemple d'utilisation
tracking = PositionTracking(initial_entry=100, trailing_stop_pips=10)
print("Nouveau stop loss :", tracking.update_stop_loss(115))
