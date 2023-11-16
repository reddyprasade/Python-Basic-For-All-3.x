class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"

class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        return self.balance

savings_account = SavingsAccount(1000, 0.03)
print("---------------Transaction------------------")
print("Check Balance:  1")
print("Deposit:        2")
print("Withdraw:       3")
print("Add Interest:   4")
print("Exit:           5")

while True:
    print("----------PLEASE CHOOSE THE OPTIONS---------")
    operation = int(input("Enter operation:")) 
    if operation == 1:
        print("Balance:",savings_account.balance)
    elif operation == 2:
        amount = float(input("Enter deposit amount:"))
        print("Balance:",savings_account.deposit(amount))
    elif operation == 3:
        amount = float(input("Enter withdraw amount:"))
        print("Balance:",savings_account.withdraw(amount))
    elif operation == 4:
        print("Balance:",savings_account.add_interest())
    elif operation == 5:
        print("Thank you for visiting us!")
        break
    else:
        print("Please enter valid options[1-5]")
        break
