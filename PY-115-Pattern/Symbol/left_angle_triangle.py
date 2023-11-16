# Shape of left angle triangle using functions
def for_left_angle_triangle():
    """ *'s printed in the shape of Left Angle Triangle """
    for row in range(9):
        for col in range(9):
            if  row +col >= 8:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


def while_left)angle_triangle():
    """ *'s printed in the shape of Left Angle Triangle """
    row =0
    while row<9:
        col =0
        while col <9:
            if  row +col >= 8:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row += 1

