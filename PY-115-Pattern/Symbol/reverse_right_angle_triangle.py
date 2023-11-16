# Shape of reverse right angle triangle using fucntions
def for_reverse_right_angle_triangle():
    """ *'s printed in the shape of Reverse Right Angle Triangle """
    for row in range(9):
        for col in range(9):
            if row+col <=8:
                print('*',end=' ')
            else:
                print(' ',end =' ')
        print()


def while_reverse_right_angle_triangle():
    """ *'s printed in the shape of Reverse Right Angle Triangle """
    row =0
    while row<9:
        col =0
        while col <9:
            if row+col <=8:
                print('*',end=' ')
            else:
                print(' ',end =' ')
            col+=1
        print()
        row += 1

