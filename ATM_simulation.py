class ATM:
    def __init__(self, balance=0, pin="1234"):
        self.balance = balance
        self.pin = pin
        self.transaction_history = []

    def check_pin(self):
        entered_pin = input("Enter your PIN: ")
        return entered_pin == self.pin

    def balance_inquiry(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def cash_withdrawal(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount:.2f}")
            print(f"Please take your cash: ${amount:.2f}")
        else:
            print("Insufficient balance.")

    def cash_deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount:.2f}")
        print(f"Deposited: ${amount:.2f}")

    def change_pin(self):
        new_pin = input("Enter new PIN: ")
        self.pin = new_pin
        print("PIN changed successfully.")

    def transaction_history_display(self):
        if not self.transaction_history:
            print("No transaction history.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)

    def run(self):
        if not self.check_pin():
            print("Incorrect PIN. Exiting.")
            return

        while True:
            print("\n1. Balance Inquiry")
            print("2. Cash Withdrawal")
            print("3. Cash Deposit")
            print("4. Change PIN")
            print("5. Transaction History")
            print("6. Exit")

            choice = input("Select an option: ")
            if choice == '1':
                self.balance_inquiry()
            elif choice == '2':
                self.cash_withdrawal()
            elif choice == '3':
                self.cash_deposit()
            elif choice == '4':
                self.change_pin()
            elif choice == '5':
                self.transaction_history_display()
            elif choice == '6':
                print("Exiting. Thank you!")
                break
            else:
                print("Invalid option. Please try again.")

# Run the ATM simulation
if __name__ == "__main__":
    atm = ATM(balance=1000)  # Initial balance can be set here
    atm.run()
