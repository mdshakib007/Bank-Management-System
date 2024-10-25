from abc import ABC

class User(ABC):
    def __init__(self, name, email, address, password) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.password = password
    

class Admin(User):
    def __init__(self, name, email, address, password) -> None:
        super().__init__(name, email, address, password)

    def delete_user_account(self, bank, user): # bank is a object of Bank class and user is an instance of GeneralUser class
        bank.delete_user_account(user)

    def show_all_users(self, bank):
        bank.show_all_users()

    def bank_balance(self, bank):
        print(f"\n\tTotal Bank balance is ${bank.bank_balance}")

    def total_loan_amount(self, bank):
        print(f"\n\tTotal Loan is ${bank.total_loan}")

    def loan_feature(self, bank, loan_type):
        bank.loan_feature(loan_type)

value = 1000
class GeneralUser(User):
    def __init__(self, name, email, address, loan_type, password) -> None:
        global value
        self.user_balance = 0
        self.loan_count = 0
        self.loan_type = loan_type
        self.transactions = [] # list of instance of 'Transaction' Class
        self.account_number = str(value + 1)
        value += 1
        super().__init__(name, email, address, password)

    def deposit(self, bank, amount):
        bank.deposit(self, amount)
    
    def withdraw(self, bank, amount):
        bank.withdraw(self, amount)

    def check_balance(self):
        print(f"\n\tMy current balance is ${self.user_balance}")

    def transaction_history(self, bank):
        bank.transaction_history(self)

    def take_a_loan(self, bank, amount):
        bank.take_a_loan(self, amount)

    def transfer_money(self, bank, user_id, amount):
        bank.transfer_money(self.account_number, user_id, amount)


