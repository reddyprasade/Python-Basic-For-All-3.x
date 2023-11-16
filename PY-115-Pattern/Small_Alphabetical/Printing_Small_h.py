for row in range(5):
		for col in range(4):
			if col==0 or row==2 and col<3 or col==3 and row>2:
				print('*', end = ' ')
			else:
				print(' ', end = ' ')
		print()
