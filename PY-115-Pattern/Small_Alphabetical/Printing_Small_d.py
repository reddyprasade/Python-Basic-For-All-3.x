for row in range(7):
		for col in range(4):
			if col==3 or col==0 and row in (4,5) or row>0 and col>0 and row%3==0:
				print('*', end = ' ')
			else:
				print(' ', end = ' ')
		print()
