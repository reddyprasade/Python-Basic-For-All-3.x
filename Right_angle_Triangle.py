row = int(input("Enter no of Rows:"))
col = int(input("Enter no of columns:"))
for i in range(row):
    for j in range(col):
        if (j==0 )or(i==3) or(i==j):
            print('*',end='')
        else:
            print(' ',end='')
    print()