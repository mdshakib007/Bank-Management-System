from users import GeneralUser, Admin
from transactions import Transaction

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
