import json
import logging

# Customer Class
class Customer:
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

# Account Class
class Account:
    def __init__(self, account_type, balance=0):
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError("Insufficient funds or invalid amount")

# Employee Class
class Employee:
    def __init__(self, employee_id, name, position):
        self.employee_id = employee_id
        self.name = name
        self.position = position

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

# Data Storage Functions
def save_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)

# Logging Configuration
logging.basicConfig(filename='logs/bank.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def log_transaction(transaction):
    logging.info(transaction)

# Initialize a list to store customers
customers = []

def create_account():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    address = input("Enter address: ")
    account_type = input("Enter account type (checking/savings): ")
    initial_deposit = float(input("Enter initial deposit: "))

    # Create a new customer and account
    customer = Customer(first_name, last_name, address)
    account = Account(account_type, initial_deposit)
    customer.add_account(account)

    # Add the customer to the list of customers
    customers.append(customer)
    print(f"Account created for {first_name} {last_name} with initial deposit of {initial_deposit}")

def deposit():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    amount = float(input("Enter deposit amount: "))

    # Find the customer
    for customer in customers:
        if customer.first_name == first_name and customer.last_name == last_name:
            # Assume the first account is the one to deposit into
            account = customer.accounts[0]
            account.deposit(amount)
            print(f"Deposited {amount} to {first_name} {last_name}'s account. New balance: {account.balance}")
            return

    print("Customer not found")

def withdraw():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    amount = float(input("Enter withdrawal amount: "))

    # Find the customer
    for customer in customers:
        if customer.first_name == first_name and customer.last_name == last_name:
            # Assume the first account is the one to withdraw from
            account = customer.accounts[0]
            try:
                account.withdraw(amount)
                print(f"Withdrew {amount} from {first_name} {last_name}'s account. New balance: {account.balance}")
            except ValueError as e:
                print(e)
            return

    print("Customer not found")

def main():
    print("Welcome to the Banking System")
    while True:
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            create_account()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()


