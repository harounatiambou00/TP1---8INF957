from PaymentStrategy import PaymentStrategy
class BankTransferPaymentStrategy(PaymentStrategy):
    def process(self, amount):
        print("Paiement par virement bancaire traité :", amount)