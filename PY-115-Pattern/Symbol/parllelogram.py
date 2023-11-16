# Shape of Parllelogram using fucntions
def for_parllelogram():
    """ *'s printed in the shape of Parllelogram """
    for row in range(9):
        for col in range(17):
            if row+col >=8 and row+col <=16:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


def while_parllelogram():
    """ *'s printed in the shape of Parllelogram """
    row =0
    while row<9:
        col =0
        while col <17:
            if row+col >=8 and row+col <=16:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row += 1

