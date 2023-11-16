for row in range(7):
		for col in range(4):
			if col==0 or row!=0 and row%3==0 and col<3 or col==3 and row in (4,5):
				print('*', end = ' ')
			else:
				print(' ', end = ' ')
		print()
