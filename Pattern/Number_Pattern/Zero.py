for row in range(5):
    for col in range(4):
        if row in {1,2,3} and col in {0,3} or row in {0,4} and col in {1,2}:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

    
### Method- 2
for i in range(7):
	for j in range(5):
		if i in (0,6) and j not in(0,4) or j in(0,4) and i not in(0,6) or i+j==5:
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print()
  
