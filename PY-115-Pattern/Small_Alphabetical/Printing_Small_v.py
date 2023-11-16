for row in range(4):
		for col in range(8):
			if row-col==0 or row+col==6:
				print('*', end = '')
			else:
				print(' ', end = '')
		print()
