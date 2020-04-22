from requests import *
from tkinter import *

# on change event
def onchange(amount):
    try:
        # assume it is a float
        amt = float(amount.get())

        # update currency
        updatecurrency(amt)
        
    except ValueError:
        global labelText
        labelText.set('Invalid Amount')

# update currency values
def updatecurrency(amount):
    global currencies, labelText, firstSelected, secondSelected

    # magic
    convertedAmt = currencies[secondSelected.get()] * amount
    outputAmt = convertedAmt / currencies[firstSelected.get()]

    # format 
    labelText.set('${:,.2f} {curr1} = ${:,.2f} {curr2}'.format(amount, outputAmt, curr1 = firstSelected.get(), curr2 = secondSelected.get()))

# switch currency function
def switchCurrencies(amount):
    first, second = firstSelected.get(), secondSelected.get()

    firstSelected.set(second)
    secondSelected.set(first)

    return onchange(amount)

# currency object 
currency = get('http://api.fixer.io/latest?base=AUD').json();

# add AUD to AUD
currency["rates"]["AUD"] = 1.0

# store all currency rates in dict
currencies = currency["rates"]

# begin TKInter
root = Tk()

# configure window
root.columnconfigure(0, weight = 1)
root.columnconfigure(2, weight = 1)
root.resizable(width = True, height = False)
root.title('Currency Converter')
root.geometry('375x75')

# amount string variable
amount = StringVar(value = "1.00")
amount.trace("w", lambda name, index, mode, amount = amount: onchange(amount))

# create list item string variables
firstSelected = StringVar(value = "AUD")
firstSelected.trace("w", lambda name, index, mode, amount = amount: onchange(amount))

secondSelected = StringVar(value = "USD")
secondSelected.trace("w", lambda name, index, mode, amount = amount: onchange(amount))

# create first currency option menu
firstCurrency = OptionMenu(root, firstSelected, *currencies.keys())
firstCurrency.grid(row = 0, column = 0, sticky=W+E)

# button between to switch
switchBtn = Button(root, text="<>", command = lambda amount = amount: switchCurrencies(amount))
switchBtn.grid(row = 0, column = 1)

# create second currency option menu
secondCurrency = OptionMenu(root, secondSelected, *currencies.keys())
secondCurrency.grid(row = 0, column = 2, sticky=W+E)

# create entry box
entryBox = Entry(root, textvariable = amount)
entryBox.grid(row = 1, column = 0, columnspan = 3, sticky=W+E+N+S)

# create label w/ label text str variable
labelText = StringVar()
label = Label(root, textvariable=labelText)
label.grid(row = 2, column = 0, columnspan = 3, sticky=W+E)

# just to auto update on initialize
onchange(amount)

root.mainloop()
