# Customer Class
from account import Account
class Customer:
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)