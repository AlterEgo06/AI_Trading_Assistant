import smtplib

class TradeNotification:
    def __init__(self, email, smtp_server="smtp.gmail.com", smtp_port=587):
        self.email = email
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_notification(self, message):
        print(f"Notification envoyée : {message}")
        # Ici, ajouter la logique d'envoi d'email si nécessaire

# Exemple d'utilisation
notifier = TradeNotification(email="trader@example.com")
notifier.send_notification("Nouvelle alerte : trade détecté avec un fort potentiel !")
