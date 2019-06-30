# height of triangle
i = int(input("Enter no Rows:"))# Row Values
j = int(input("Enter no of columns:"))
for row in range(i):
    for col in range(j):
        if (row==0 and col==2)or(row==1 and col%2!=0)or(row==2):
            print('*',end='')
        else:
            print(" ",end='')
    print()