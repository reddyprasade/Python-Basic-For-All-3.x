for row in range(6):
		for col in range(4):
			if col>0 and col<2 and row%3==0 or col==0 and row in (1,2) or col==2 or col==3 and row==4:
				print('*', end = ' ')
			else:
				print(' ', end = ' ')
		print() 
