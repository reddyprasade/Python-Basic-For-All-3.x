i=0
j=4
for row in range(7):
    for col in range(5):
        if col==0 or (row==col+2 and col>1):
            print("*",end="")
        elif((row==i and col==j) and col>0):
            print("*",end="")
            i=i+1
            j=j-1
        else:
            print(end=" ")
    print()
