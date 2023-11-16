n=20
for i in range(1, 11):
    print(' '*n, end='') # repet space for n times
    print('* '*(i)) # repeat stars for i times
    n-=1
    
    
    
### Method - 2 

n=20
for i in range(1, 11):
    print(' '*(n-i) + '* '*(i))
