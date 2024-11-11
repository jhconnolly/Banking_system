from customer import Customer
from account import Account
from data_storage import save_data, load_data
from logger import log_transaction

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