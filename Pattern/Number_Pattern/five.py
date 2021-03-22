for row in range(7):
    for col in range(4):
        if row==0 or row in {1,2} and col<1 or row in{4,5} and col>2 or row in {3,6} and col<3:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
 ### Method-5

for i in range(6):
	for j in range(5):
		if i==0 or i==2 and j<4 or j==0 and i<3 or j==4 and i in(3,4) or i==5 and j<4 :
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print()
