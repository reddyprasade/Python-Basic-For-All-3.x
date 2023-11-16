for row in range(7):
		for col in range(4):
			if col==0 or row+col==4 or row-col==3:
				print('*', end = ' ')
			else:
				print(' ', end = ' ')
		print()
