for row in range(6):
		for col in range(3):
			if col==0 and row==5 or col==1 and row!=5 or col==2 and row==5:
				print('*', end = ' ')
			else:
				print(' ', end = ' ')
		print()
