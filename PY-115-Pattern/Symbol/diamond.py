# Shape of Diamond using functions using fucntions
def for_diamond():
    """ *'s printed in the shape of Diamond """
    for row in range(17):
        for col in range(17):
            if row+col>=8 and col -row <=8 and row -col <=8 and row+col <=24 :
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_diamond():
    """ *'s printed in the shape of Diamond """
    row =0
    while row<17:
        col =0
        while col <17:
            if row+col>=8 and col -row <=8 and row -col <=8 and row+col <=24 :
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row += 1

while_diamond()
for_diamond()
