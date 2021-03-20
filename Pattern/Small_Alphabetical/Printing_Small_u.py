for row in range(4):
		for col in range(4):
			if col%3==0 and row<3 or row==3 and col>0:
				print('*', end = ' ')
			else:
				print(' ', end = ' ')
		print()
