class ATM:
    def __init__(self, account):
        self.account = account

    def login(self):
        for attempt in range(3):
            entered_pin = input("Enter your PIN: ")

            if entered_pin == self.account["pin"]:
                print("Login successful!")
                print("Welcome", self.account["name"])
                return True

            print("Wrong PIN.")

        print("Too many wrong attempts.")
        print("Your card has been blocked.")
        return False

    def check_balance(self):
        print("\nCurrent balance: ₹", self.account["balance"])

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: ₹"))
        except ValueError:
            print("Please enter a valid amount.")
            return

        if amount <= 0:
            print("Please enter a valid amount.")
        elif amount > self.account["balance"]:
            print("Insufficient balance.")
        elif amount % 100 != 0:
            print("Please enter an amount in multiples of 100.")
        else:
            self.account["balance"] -= amount
            self.account["transactions"].append("Withdrawn: ₹" + str(amount))
            print("Please collect your cash.")
            print("Remaining balance: ₹", self.account["balance"])

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: ₹"))
        except ValueError:
            print("Please enter a valid amount.")
            return

        if amount <= 0:
            print("Please enter a valid amount.")
        else:
            self.account["balance"] += amount
            self.account["transactions"].append("Deposited: ₹" + str(amount))
            print("Amount deposited successfully.")
            print("New balance: ₹", self.account["balance"])

    def change_pin(self):
        old_pin = input("Enter your current PIN: ")

        if old_pin != self.account["pin"]:
            print("Incorrect current PIN.")
            return

        new_pin = input("Enter your new 4-digit PIN: ")

        if len(new_pin) == 4 and new_pin.isdigit():
            self.account["pin"] = new_pin
            print("PIN changed successfully.")
        else:
            print("PIN must contain exactly 4 digits.")

    def mini_statement(self):
        print("\n========== MINI STATEMENT ==========")

        if not self.account["transactions"]:
            print("No transactions available.")
        else:
            for transaction in self.account["transactions"]:
                print(transaction)

        print("------------------------------------")
        print("Current Balance: ₹", self.account["balance"])
        print("====================================")
