# Shape of reverse equilateral triangle using functions
def for_reverse_equilateral_triangle():
    """ *'s printed in the shape of Reverse Triangle """
    for row in range(9):
        for col in range(17):
            if row<=col and row+col<=16:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


def while_reverse_equilateral_triangle():
    """ *'s printed in the shape of Reverse Triangle """
    row =0
    while row<9:
        col =0
        while col <17:
            if row<=col and row+col<=16:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row += 1

