from PaymentStrategy import PaymentStrategy
class CreditCardPaymentStrategy(PaymentStrategy):
    def process(self, amount):
        print("Paiement par carte de crédit traité :", amount)