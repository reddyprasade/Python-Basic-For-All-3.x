for row in range(7):
    for col in range(4):
        if row==0 and col in {1,2} or row in {1,2,4,5} and col<1 or row in {3} and col in {0,1,2} or row in {4,5} and col>2 or row==6 and col in {1,2}:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
