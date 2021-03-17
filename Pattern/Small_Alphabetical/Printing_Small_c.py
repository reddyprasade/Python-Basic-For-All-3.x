for row in range(4):
		for col in range(4):
			if col==0 and row%3!=0 or col>0 and row%3==0:
				print('*', end = ' ')
			else:
				print(' ', end = ' ')
		print()
