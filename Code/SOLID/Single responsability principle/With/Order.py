from EmailService import EmailService

class Order:
    def __init__(self, items, customer):
        self.items = items
        self.customer = customer

    def create_order(self):
        # Logique de création de la commande dans la base de données
        emailService = EmailService()
        emailService.send_email("Votre commande a bien ete creee.")
