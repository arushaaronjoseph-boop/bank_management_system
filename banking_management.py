
from abc import ABC, abstractmethod
import csv


# Abstract class for common user information
class Person(ABC):

    def __init__(self, name):
        self._name = name

    # Child classes must implement this method
    @abstractmethod
    def display_info(self):
        pass


# Customer class inherits Person
class Customer(Person):

    def __init__(self, customer_id, name):

        # Calling parent class constructor
        super().__init__(name)

        # Private customer ID
        self.__customer_id = customer_id

    # Display customer information
    def display_info(self):

        print("Customer ID:", self.__customer_id)
        print("Name:", self._name)

    # Getter for customer ID
    def get_customer_id(self):
        return self.__customer_id


# BankAccount class handles account details
class BankAccount:

    def __init__(self, account_number, customer_id, account_type, pin):

        # Private account details
        self.__account_number = account_number
        self.__customer_id = customer_id
        self.__account_type = account_type
        self.__pin = pin
        self.__balance = 0

    # Display account details
    def display_info(self):

        print("Account Number:", self.__account_number)
        print("Customer ID:", self.__customer_id)
        print("Account Type:", self.__account_type)
        print("Balance:", self.__balance)

    # Getter for account number
    def get_account_number(self):
        return self.__account_number

    # Getter for customer ID
    def get_customer_id(self):
        return self.__customer_id

    # Getter for account type
    def get_account_type(self):
        return self.__account_type

    # Getter for balance
    def get_balance(self):
        return self.__balance

    # Getter for PIN
    def get_pin(self):
        return self.__pin

    # Setter for balance
    def set_balance(self, balance):
        self.__balance = balance

    # Check account PIN
    def check_pin(self, pin):
        return self.__pin == pin

    # Deposit money
    def deposit(self, amount):

        if amount > 0:

            self.__balance += amount
            return True

        return False

    # Withdraw money
    def withdraw(self, amount):

        # Check available balance
        if amount > 0 and amount <= self.__balance:

            self.__balance -= amount
            return True

        return False


# Transaction class stores transaction records
class Transaction:

    def __init__(self, transaction_id, account_number, transaction_type, amount):

        self.__transaction_id = transaction_id
        self.__account_number = account_number
        self.__transaction_type = transaction_type
        self.__amount = amount

    # Display transaction details
    def display_info(self):

        print("Transaction ID:", self.__transaction_id)
        print("Account Number:", self.__account_number)
        print("Type:", self.__transaction_type)
        print("Amount:", self.__amount)

    # Getter for transaction ID
    def get_transaction_id(self):
        return self.__transaction_id

    # Getter for account number
    def get_account_number(self):
        return self.__account_number

    # Getter for transaction type
    def get_transaction_type(self):
        return self.__transaction_type

    # Getter for transaction amount
    def get_amount(self):
        return self.__amount


# Class to manage bank operations
class Bank_Management:

    def __init__(self):

        self.customers = []
        self.accounts = []
        self.transactions = []

        # Account numbers will start from 10001
        self.account_number = 10000
        self.transaction_number = 1

    # Add new customer
    def add_customer(self):

        try:

            customer_id = int(input("Enter Customer ID: "))
            name = input("Enter Customer Name: ")

            customer = Customer(
                customer_id,
                name
            )

            self.customers.append(customer)

            print("Customer added successfully.")

        except ValueError:

            print("Please enter a valid Customer ID.")

    # Create bank account
    def create_account(self):

        try:

            customer_id = int(input("Enter Customer ID: "))

            customer_found = False

            for customer in self.customers:

                if customer.get_customer_id() == customer_id:

                    customer_found = True
                    break

            if customer_found:

                account_type = input(
                    "Enter Account Type (Savings/Current): "
                )

                pin = input("Create a 4-digit PIN: ")

                if len(pin) != 4 or not pin.isdigit():

                    print("PIN must contain exactly 4 digits.")
                    return

                # Generate account number automatically
                self.account_number += 1

                account = BankAccount(
                    self.account_number,
                    customer_id,
                    account_type,
                    pin
                )

                self.accounts.append(account)

                print("Account created successfully.")
                print("Account Number:", self.account_number)

            else:

                print("Customer not found.")

        except ValueError:

            print("Invalid input.")

    # Find account and verify PIN
    def find_account(self):

        try:

            account_number = int(input("Enter Account Number: "))
            pin = input("Enter PIN: ")

            for account in self.accounts:

                if account.get_account_number() == account_number:

                    if account.check_pin(pin):

                        return account

                    else:

                        print("Incorrect PIN.")
                        return None

            print("Account not found.")
            return None

        except ValueError:

            print("Please enter a valid Account Number.")
            return None

    # Deposit money
    def deposit_money(self):

        account = self.find_account()

        if account is None:
            return

        try:

            amount = float(input("Enter Deposit Amount: "))

            if account.deposit(amount):

                transaction = Transaction(
                    self.transaction_number,
                    account.get_account_number(),
                    "Deposit",
                    amount
                )

                self.transactions.append(transaction)

                self.transaction_number += 1

                print("Money deposited successfully.")

            else:

                print("Please enter a valid amount.")

        except ValueError:

            print("Please enter a valid amount.")

    # Withdraw money
    def withdraw_money(self):

        account = self.find_account()

        if account is None:
            return

        try:

            amount = float(input("Enter Withdrawal Amount: "))

            if account.withdraw(amount):

                transaction = Transaction(
                    self.transaction_number,
                    account.get_account_number(),
                    "Withdraw",
                    amount
                )

                self.transactions.append(transaction)

                self.transaction_number += 1

                print("Money withdrawn successfully.")

            else:

                print("Insufficient balance or invalid amount.")

        except ValueError:

            print("Please enter a valid amount.")

    # Check balance
    def check_balance(self):

        account = self.find_account()

        if account is None:
            return

        print("Current Balance:", account.get_balance())

    # Show transaction history
    def show_transactions(self):

        account = self.find_account()

        if account is None:
            return

        account_number = account.get_account_number()
        found = False

        for transaction in self.transactions:

            if transaction.get_account_number() == account_number:

                transaction.display_info()
                print()

                found = True

        if not found:

            print("No transactions found.")

    # Save all records
    def save_records(self):

        with open("customers.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Customer_ID",
                "Name"
            ])

            for customer in self.customers:

                writer.writerow([
                    customer.get_customer_id(),
                    customer._name
                ])

        with open("accounts.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Account_Number",
                "Customer_ID",
                "Account_Type",
                "PIN",
                "Balance"
            ])

            for account in self.accounts:

                writer.writerow([
                    account.get_account_number(),
                    account.get_customer_id(),
                    account.get_account_type(),
                    account.get_pin(),
                    account.get_balance()
                ])

        with open("transactions.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Transaction_ID",
                "Account_Number",
                "Type",
                "Amount"
            ])

            for transaction in self.transactions:

                writer.writerow([
                    transaction.get_transaction_id(),
                    transaction.get_account_number(),
                    transaction.get_transaction_type(),
                    transaction.get_amount()
                ])

        print("Records saved successfully.")

    # Load records
    def load_records(self):

        try:

            with open("customers.csv", "r") as file:

                reader = csv.DictReader(file)

                for row in reader:

                    customer = Customer(
                        int(row["Customer_ID"]),
                        row["Name"]
                    )

                    self.customers.append(customer)

            with open("accounts.csv", "r") as file:

                reader = csv.DictReader(file)

                for row in reader:

                    account = BankAccount(
                        int(row["Account_Number"]),
                        int(row["Customer_ID"]),
                        row["Account_Type"],
                        row["PIN"]
                    )

                    # Restore saved balance
                    account.set_balance(
                        float(row["Balance"])
                    )

                    self.accounts.append(account)

                    # Keep account number ready for next new account
                    if int(row["Account_Number"]) > self.account_number:
                        self.account_number = int(row["Account_Number"])

            with open("transactions.csv", "r") as file:

                reader = csv.DictReader(file)

                for row in reader:

                    transaction = Transaction(
                        int(row["Transaction_ID"]),
                        int(row["Account_Number"]),
                        row["Type"],
                        float(row["Amount"])
                    )

                    self.transactions.append(transaction)

                    # Keep transaction number ready
                    if int(row["Transaction_ID"]) >= self.transaction_number:
                        self.transaction_number = int(row["Transaction_ID"]) + 1

            print("Records loaded successfully.")

        except FileNotFoundError:

            print("File not found.")

    # Menu system
    def menu(self):

        while True:

            print("\n--- Bank Account Management System ---")

            print("1. Add Customer")
            print("2. Create Account")
            print("3. Deposit Money")
            print("4. Withdraw Money")
            print("5. Check Balance")
            print("6. Transaction History")
            print("7. Save Records")
            print("8. Load Records")
            print("9. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":

                self.add_customer()

            elif choice == "2":

                self.create_account()

            elif choice == "3":

                self.deposit_money()

            elif choice == "4":

                self.withdraw_money()

            elif choice == "5":

                self.check_balance()

            elif choice == "6":

                self.show_transactions()

            elif choice == "7":

                self.save_records()

            elif choice == "8":

                self.load_records()

            elif choice == "9":

                print("Program ended.")
                break

            else:

                print("Invalid choice.")


# Start Bank Management System
system = Bank_Management()
system.menu()