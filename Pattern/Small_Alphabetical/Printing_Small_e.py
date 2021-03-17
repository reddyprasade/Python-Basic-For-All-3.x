  	for row in range(7):
		for col in range(6):
			if col==0 and row>0 and row<6 or col>0 and col<5 and row%3==0 or col==5 and row in (1,2):
				print('*', end = ' ')
			else:
				print(' ', end = ' ')
		print()
