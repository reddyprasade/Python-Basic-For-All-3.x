for row in range(7):
    for col in range(4):
     if row+col==4 or row==6 or row==0 and col in {1,2} or row==1 and col<1 or row==5 and col<1:
        print('*',end=' ')
     else:
         print(' ',end=' ')
    print()
    
### Method-2
for i in range(7):
	for j in range(5):
		if i==6 or i+j==6 or i==0 and j not in(0,4) or i==1 and j in(0,4):
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print()
     
