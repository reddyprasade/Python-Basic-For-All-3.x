for row in range(4):
		for col in range(4):
			if row%3==0 and col in (1,2) or col%3==0 and row in (1,2):
				print('*', end = ' ')
			else:
				print(' ', end = ' ')	
		print()
