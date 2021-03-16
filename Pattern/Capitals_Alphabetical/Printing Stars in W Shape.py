#W 
for row in range(6):
    for col in range(6):
        if (col==0 or col==5) or (row+col==5 and row>2)or(row-col==0 and row>2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

    
# Method- 2 

i = 0
j = 3
for row in range(4):
    for col in range(7):
        if col==0 or col==6 or (col==5 and row==2)or(col==4 and row==1):
            print('*',end=' ')
        elif row==i and col==j:
            print('*',end=' ')
            i+=1
            j-=1
        else:
            print(' ',end=' ')
    print()
