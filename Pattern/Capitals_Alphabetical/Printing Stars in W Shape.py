#W 
for row in range(6):
    for col in range(6):
        if (col==0 or col==5) or (row+col==5 and row>2)or(row-col==0 and row>2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
