# Shape of Equilateral Triangle using fucntions
def for_equilateral_triangle():
    """ *'s printed in the shape of Equilateral Triangle """
    for row in range(9):
        for col in range(15):
            if row+col >=8 and col-row<7:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
def while_equilateral_triangle():
    """ *'s printed in the shape of Equilateral Triangle """
    row =0
    while row<9:
        col =0
        while col <15:
            if row+col >=8 and col-row<7:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row += 1

