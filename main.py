from datetime import datetime
from abc import ABC


class Transaction:
    def __init__(self, name, trax_type, traxid, amount):
        self.name = name
        self.trax_type = trax_type
        self.traxid = traxid
        self.amount = amount
        self.time = datetime.now()


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


class Bank:
    '''This class is maintaining all the application related to Shop'''
    def __init__(self, name, init_balance) -> None:
        self.name = name        # bank name
        self.general_users = [] #--> instance of 'GeneralUser' class
        self.admins = []        #--> instance of 'Admin' class
        self.__bank_balance = init_balance
        self.__total_loan = 0
        self.__loan_open = True

    def user_register(self, name, email, address, loan_type, password):
        for user in self.general_users:
            if user.email == email:
                print("\n\tThis email is already taken!")
                return None
        
        user = GeneralUser(name, email, address, loan_type, password)
        self.general_users.append(user)
        print(f"\n\tRegistration Successful with account number: {user.account_number}")
        return user

    def user_login(self, email, password):
        for user in self.general_users:
            if user.email == email and user.password == password:
                print("\n\tLogin successfun!")
                return user
        print("\n\tIncorrect email or password!")
        return None

    def admin_register(self, name, email, address, password):
        for admin in self.admins:
            if admin.email == email:
                print("\n\tThis email is already taken!")
                return None
        
        admin = Admin(name, email, address, password)
        self.admins.append(admin)
        print("\n\tRegistration Successful!")
        return admin

    def admin_login(self, email, password):
        for admin in self.admins:
            if admin.email == email and admin.password == password:
                print("\n\tLogin successfun!")
                return admin
        print("\n\tIncorrect email or password!")
        return None

    def delete_user_account(self, user_id):
        found = False
        for g_user in self.general_users:
            if g_user.account_number == user_id:
                found = True
                self.bank_balance += g_user.user_balance
                self.general_users.remove(g_user)
                print("\n\tUser deleted!")
                break
        if not found:
            print("\n\tUser not found!")

    def show_all_users(self):
        print("\n\tAll users...")
        for user in self.general_users:
            print(f"\n\tAccount number: {user.account_number} - Name: {user.name} - Email: {user.email}")
    
    @property
    def bank_balance(self):
        return self.__bank_balance
    
    @bank_balance.setter
    def bank_balance(self, amount):
        self.__bank_balance += amount

    @property
    def total_loan(self):
        return self.__total_loan
    
    def loan_feature(self, type):
        self.__loan_open = type
        if(type == True):
            print("\n\tLoan feature is enabled!")
        else:
            print("\n\tLoan feature is disabled!")

    def deposit(self, user, amount):
        if amount > 0:
            user.user_balance += amount
            self.__bank_balance += amount
            transaction = Transaction(user.name, "IN", len(user.transactions)+1000, amount)
            user.transactions.append(transaction)
            print(f"\n\t${amount} deposit successful!")
            print(f"\n\tCurrent balance: ${user.user_balance}")
        else:
            print("\n\tAmount is too low to deposit!")

    def withdraw(self, user, amount):
        if user.user_balance >= amount and amount > 0:
            user.user_balance -= amount
            self.__bank_balance -= amount
            transaction = Transaction(user.name, "OUT", len(user.transactions)+1000, amount)
            user.transactions.append(transaction)
            print(f"\n\t${amount} withdraw successful!")
        else:
            print("\n\tInsufficient amount!")
    
    def transaction_history(self, user):
        print("\n\tMy transactions...")
        for trax in user.transactions:
            print(f"\n\t{trax.name}({trax.traxid}) - {trax.trax_type} - ${trax.amount} - {trax.time}")

    def take_a_loan(self, user, amount):
        if self.__loan_open == False:
            print("\n\tLoan feature is not available right now!")
            return None
            
        if amount <= 100000 and amount >= 10 and self.__bank_balance >= amount:
            if user.loan_count >= 2:
                print("\n\tMaximum loan taken!")
            else:
                user.user_balance += amount
                self.__bank_balance -= amount
                self.__total_loan += amount
                user.loan_count += 1
                print(f"\n\t${amount} is taken as loan!")
        else:
            print("\n\tInvalid amount or bank balance is low!")

    def transfer_money(self, user1_id, user2_id, amount):
        if amount < 1:
            print("\n\tInvalid amount!")
            return None
        
        user1 = None
        user2 = None
        for user in self.general_users:
            if user.account_number == user1_id:
                user1 = user
            elif user.account_number == user2_id:
                user2 = user

        if user1 is None or user2 is None or user1_id == user2_id:
            print("\n\tUser not found or same user!")
            return None

        if user1.user_balance >= amount:
            user1.user_balance -= amount
            user2.user_balance += amount
            print(f"\n\t${amount} transfer successful to {user2.name}")
        else:
            print("\n\tNot enough money to transfer!")




aspire_bank = Bank("Aspire-Bank", 10000000)
curr_user = None
is_admin = False

while True:
    if curr_user == None:
        print(f"\n--------Welcome to {aspire_bank.name}---------")
        print("1. User Registration")
        print("2. User Login")
        print("3. Admin Registration")
        print("4. Admin Login")
        print("5. Exit")

        op = input(">>> ")
        if op == "1":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            loan_type = input("Loan type: (Savings/Current) S/C: ")
            password = input("Password: ")
            curr_user = aspire_bank.user_register(name, email, address, loan_type, password)

            if curr_user != None:
                is_admin = False

        elif op == "2":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            curr_user = aspire_bank.user_login(email, password)

            if curr_user != None:
                is_admin = False

        if op == "3":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            password = input("Password: ")
            curr_user = aspire_bank.admin_register(name, email, address, password)

            if curr_user != None:
                is_admin = True

        elif op == "4":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            curr_user = aspire_bank.admin_login(email, password)

            if curr_user != None:
                is_admin = True
        
        elif op == "5":
            exit()

    else:
        if is_admin:
            print("\n------Admin Menu-------")
            print(f"@{curr_user.email}")
            print("1. Delete User Account")
            print("2. Show All Users")
            print("3. Check Bank Balance")
            print("4. Check Total Loan Given")
            print("5. ON/OFF Loan Feature")
            print("6. Log Out")
            
            op = input(">>> ")
            if op == "1":
                user_id = input("Enter user account number: ")
                curr_user.delete_user_account(aspire_bank, user_id)


            elif op == "2":
                curr_user.show_all_users(aspire_bank)
            
            elif op == "3":
                curr_user.bank_balance(aspire_bank)
            
            elif op == "4":
                curr_user.total_loan_amount(aspire_bank)

            elif op == "5":
                print("\n\t1. ON")
                print("\t2. OFF")

                cmd = input("\t> ")
                loan_type = True
                if(cmd == "2"):
                    loan_type = False

                curr_user.loan_feature(aspire_bank, loan_type)
            
            elif op == "6":
                print(f"\n\t@{curr_user.email} Logged out!")
                curr_user = None
            
            else:
                print("\n\tInvalid input!")

        else:
            print("\n-------User Menu-------")
            print(f"Account Number: @{curr_user.account_number}")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transaction History")
            print("5. Take a Loan")
            print("6. Transfer Money")
            print("7. Logout")

            op = input(">>> ")
            if op == "1":
                amount = int(input("Enter amount to deposit: "))
                curr_user.deposit(aspire_bank, amount)
            
            elif op == "2":
                amount = int(input("Enter amount to withdraw: "))
                curr_user.withdraw(aspire_bank, amount)

            elif op == "3":
                curr_user.check_balance()
            
            elif op == "4":
                curr_user.transaction_history(aspire_bank)

            elif op == "5":
                amount = int(input("Enter amount: $"))
                curr_user.take_a_loan(aspire_bank, amount)
            
            elif op == "6":
                user_id = input("Enter user account number: ")
                amount = int(input("Enter amount: "))
                curr_user.transfer_money(aspire_bank, user_id, amount)

            elif op == "7":
                print(f"\n\t@{curr_user.account_number} Logged out!")
                curr_user = None
            
            else:
                print("\n\tInvalid input!")
