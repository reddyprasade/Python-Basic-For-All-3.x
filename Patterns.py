# Heart shape Patterens 
#for row in range(6):
#    for col in range(7):
#        if(row ==0 and col%3!=0)or(row==1 and col%3==0)or(row-col==2)or(row+col==8):
#            print("*",end=' ')
#        else:
#            print(" ",end=' ')
#    print()

# Triangle
for row in range(3):
    for col in range(5):
        if(row==0 and col==2)or (row==1 and col%2!=0)or(row==2):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()