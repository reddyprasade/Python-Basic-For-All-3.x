balance1 = 0
balance2 = 0
balance3 = 0
balance4 = 0
balance5 = 0

def firstDeposit(amount):
    global balance1
    balance1 += amount

def secondDeposit(amount):
    global balance2
    balance2 += amount

def thirdDeposit(amount):
    global balance3
    balance3 += amount

def fourthDeposit(amount):
    global balance4
    balance4 += amount

def fifthDeposit(amount):
    global balance5
    balance5 += amount

def firstWithdraw(amount):
    global balance1
    if balance1 >= amount:
        balance1 -= amount
    else:
        print("Insufficient funds.")

def secondWithdraw(amount):
    global balance2
    if balance2 >= amount:
        balance2 -= amount
    else:
        print("Insufficient funds.")

def thirdWithdraw(amount):
    global balance3
    if balance3 >= amount:
        balance3 -= amount
    else:
        print("Insufficient funds.")

def fourthWithdraw(amount):
    global balance4
    if balance4 >= amount:
        balance4 -= amount
    else:
        print("Insufficient funds.")

def fifthWithdraw(amount):
    global balance5
    if balance5 >= amount:
        balance5 -= amount
    else:
        print("Insufficient funds.")
        
def firstBalance():
    global balance1
    print("Your current balance is:", balance1) 

def secondBalance():
    global balance2
    print("Your current balance is:", balance2)

def thirdBalance():
    global balance3
    print("Your current balance is:", balance3)

def fourthBalance():
    global balance4
    print("Your current balance is:", balance4)

def fifthBalance():
    global balance5
    print("Your current balance is:", balance5) 

#First Client transaction 
firstDeposit(100)
firstWithdraw(50)
firstBalance()

#Second Client Transaction
secondDeposit(200)
secondWithdraw(100)
secondBalance()
    
#Third Client Transaction
thirdDeposit(500)
thirdWithdraw(300)
thirdBalance()

#Fourth Client Transaction
fourthDeposit(1000)
fourthWithdraw(100)
fourthBalance()

#Fifth Client Transaction
fifthDeposit(200)
fifthWithdraw(300)
fifthBalance()



