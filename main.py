from atm import ATM
from data import accounts

print("====================================")
print("       ATM MANAGEMENT SYSTEM")
print("====================================")

account_number = input("Enter account number: ")

if account_number not in accounts:
    print("Account not found.")
    exit()

account = accounts[account_number]
atm = ATM(account)

if not atm.login():
    exit()

while True:
    print("\n========== ATM MENU ==========")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Change PIN")
    print("5. Mini Statement")
    print("6. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        atm.check_balance()

    elif choice == "2":
        atm.withdraw()

    elif choice == "3":
        atm.deposit()

    elif choice == "4":
        atm.change_pin()

    elif choice == "5":
        atm.mini_statement()

    elif choice == "6":
        print("\nThank you for using our ATM.")
        print("Have a nice day!")
        break

    else:
        print("Invalid choice. Please try again.")
