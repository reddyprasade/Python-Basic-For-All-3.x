for row in range(7):
    for col in range(4):
        if col==3 or row in {0,3,6} and col in {0,1,2}:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
#### Method-2
for i in range(7):
	for j in range(4):
		if i%3==0 and j<3 or j==3 and i%3!=0:
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print()
