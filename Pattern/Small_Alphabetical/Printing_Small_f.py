for row in range(6):
		for col in range(4):
			if col==1 and row>0 or row==3 and col<3 or col==2 and row==0 or col==3 and row==1:
				print('*', end = ' ')
			else:
				print(' ', end = ' ')
		print()
