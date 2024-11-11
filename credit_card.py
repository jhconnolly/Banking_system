# CreditCard Class
class CreditCard:
    def __init__(self, card_number, customer, credit_limit):
        self.card_number = card_number
        self.customer = customer
        self.credit_limit = credit_limit
        self.balance = 0

    def charge(self, amount):
        if self.balance + amount <= self.credit_limit:
            self.balance += amount
            return self.balance
        else:
            raise ValueError("Credit limit exceeded")

    def make_payment(self, amount):
        if amount > 0:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError("Payment amount must be positive")