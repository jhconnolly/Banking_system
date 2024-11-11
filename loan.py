# Loan Class
class Loan:
    def __init__(self, loan_id, customer, amount, interest_rate):
        self.loan_id = loan_id
        self.customer = customer
        self.amount = amount
        self.interest_rate = interest_rate
        self.balance = amount

    def make_payment(self, amount):
        if amount > 0:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError("Payment amount must be positive")
