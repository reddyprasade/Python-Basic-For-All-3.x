for row in range(6):
		for col in range(4):
			if col==2 and row!=1 and row!=5 or row==5 and col==1 or col==0 and row==4 or col==1 and row==2:
				print('*', end = ' ')
			else:
				print(' ', end = ' ')
		print()
