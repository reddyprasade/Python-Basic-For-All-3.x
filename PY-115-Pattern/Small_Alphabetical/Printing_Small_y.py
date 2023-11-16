for row in range(7):
		for col in range(5):
			if col==4 or row>0 and col>0 and col<6 and row%3==0 or col==0 and (row<3 or row==5):
				print('*', end = ' ')
			else:
				print(' ', end = ' ')
		print()
