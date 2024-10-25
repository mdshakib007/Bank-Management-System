from bank import Bank

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
