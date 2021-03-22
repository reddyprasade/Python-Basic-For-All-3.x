for row in range(7):
    for col in range(4):
     if row+col==4 or row==6 or row==0 and col in {1,2} or row==1 and col<1 or row==5 and col<1:
        print('*',end=' ')
     else:
         print(' ',end=' ')
    print()
     
