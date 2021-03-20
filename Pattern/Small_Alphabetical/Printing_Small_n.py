for row in range(4):
		for col in range(3):
			if row==0 and col in (0,1) or row>0 and col%2==0:
				print('*', end = ' ')
			else:
				print(' ', end = ' ')
		print()
