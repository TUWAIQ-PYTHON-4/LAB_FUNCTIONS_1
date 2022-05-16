
def pattern_num(num:int):
    '''
    this function used to printing the number in hierarchical pattern
    '''
    for i in range (num, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print ("")
        

pattern_num(5)
print(pattern_num.__doc__)