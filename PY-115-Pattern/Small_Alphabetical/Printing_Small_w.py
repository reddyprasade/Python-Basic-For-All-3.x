for row in range(5):
		for col in range(7):
			if col in (0,6) and row<4 or row==4 and col%3!=0 or col==3 and row in (2,3):
				print('*', end = ' ')
			else:
				print(' ', end = ' ')
		print()
