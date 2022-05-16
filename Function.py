

def Pyramid(rows=int):
    '''
    this function used to order number
    '''

    for i in range(0,rows + 1):
        for j in range(rows - i,0,-1):
            print( j,end=' ')
        print()
Pyramid(5)
print(Pyramid.__doc__)