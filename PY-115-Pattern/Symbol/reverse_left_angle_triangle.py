# Shape of reverse left angle triangle using fucntions
def for_reverse_left_angle_triangle():
    """ *'s printed in the shape of Reverse Left Angle Triangle """
    for row in range(9):
        for col in range(9):
            if col >= row:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


def while_reverse_left_angle_triangle():
    """ *'s printed in the shape of Reverse Left Angle Triangle """
    row =0
    while row<9:
        col =0
        while col <9:
            if col >= row:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row += 1

