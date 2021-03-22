 ##Pattern program for Number "1"
 for row in range(5):
     for col in range(4):
         if col==2 or (row==1 and col>0 and col<3) or (row==4 and col>0):
            print('*',end=' ')
         else:
             print(' ',end=' ')
     print()
