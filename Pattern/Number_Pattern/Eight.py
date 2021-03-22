for row in range(7):
    for col in range(4):
         if row in{0,3,6} and col in {1,2} or (row in {1,2,4,5} and col in{0,3}):
             print('*',end=' ')
         else:
             print(' ',end=' ')
    print()
