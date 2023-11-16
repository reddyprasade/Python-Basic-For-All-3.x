class BankAccount:
    def __init__(self):
        self.balance = 0  

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print("Your current balance is:", self.balance)

#First client
client_1 = BankAccount()#Creation of objects
client_1.deposit(100) #Invoking deposit method of client_1
client_1.withdraw(50) #Invoking withdraw method of client_1
client_1.check_balance() #Invoking check_balance method of client_1 

#Second client
client_2 = BankAccount()
client_2.deposit(200)
client_2.withdraw(50)
client_2.check_balance()



