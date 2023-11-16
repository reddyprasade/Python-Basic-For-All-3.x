balance = 0
balance1 = 0

def firstDeposit(amount):
    global balance
    balance += amount

def secondDeposit(amount):
    global balance1
    balance1 += amount

def firstWithdraw(amount):
    global balance
    if balance >= amount:
        balance -= amount
    else:
        print("Insufficient funds.")

def secondWithdraw(amount):
    global balance1
    if balance1 >= amount:
        balance1 -= amount
    else:
        print("Insufficient funds.")
        
def firstBalance():
    global balance
    print("Your current balance is:", balance) #must print "Your current balance is 50"

def secondBalance():
    global balance1
    print("Your current balance is:", balance1) #must print "Your current balance is 100"

#First Client transaction 
firstDeposit(100)
firstWithdraw(50)
firstBalance()

#Second Client Transaction
secondDeposit(200)
secondWithdraw(100)
secondBalance()


