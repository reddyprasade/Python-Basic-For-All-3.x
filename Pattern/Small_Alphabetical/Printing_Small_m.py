for row in range(4):
		for col in range(5):
			if row==0 and (col==0 or col%2!=0) or row>0 and col%2==0:
				print('*', end = ' ')
			else:
				print(' ', end = ' ')
		print()
