for row in range(5):
		for col in range(4):
			if row==0 and col!=1 or col==1 and row>0:
				print('*', end = ' ')
			else:
				print(' ', end = ' ')
		print()
