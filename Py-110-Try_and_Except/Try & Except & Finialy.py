##def askint():
##        try:
##            val = int(input("Please enter an integer: "))
##        except:
##            print ("Looks like you did not enter an integer!")
##            
##        finally:
##            print ("Finally, I executed!")
##        print ("Given Input is ",val)
##
##askint()


def askint1():
        try:
            val = int(input("Please enter an integer: "))
        except:
            print ("Looks like you did not enter an integer!")
            val = int(input("Try again-Please enter an integer: "))
        finally:
            print ("Finally, I executed!")
        print(val)
askint1()
