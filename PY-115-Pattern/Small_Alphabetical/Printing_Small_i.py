for row in range(6):
		for col in range(4):
			if col==2 and row!=1 or row==5 and col>0 or col==1 and row==3:
				print('*', end = ' ')
			else:
				print(' ', end = ' ')
		print()
