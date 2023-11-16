for row in range(7):
    for col in range(4):
        if col==3 or row==3 and col in {0,1,2} or row in {0,1,2} and col<1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
    
 ### Method-4

for i in range(6):
	for j in range(6):
		if j==3 or i+j==3 or i==3:
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print()
 
### 
