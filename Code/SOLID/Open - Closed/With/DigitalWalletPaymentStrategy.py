from PaymentStrategy import PaymentStrategy
class DigitalWalletPaymentStrategy(PaymentStrategy):
    def process(self, amount):
        print("Paiement par portefeuille numérique traité :", amount)