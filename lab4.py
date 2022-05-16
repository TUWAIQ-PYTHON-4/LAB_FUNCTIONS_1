def printer(number:int):
 ''' function that takes 1 parameter of type int ,
 then it prints out the hirarchical pattern
     '''
 for i in range(number,0,-1):
    for j in range(i,0,-1):
        print(j, end=' ')
    print('')
printer(9)
print(printer.__doc__)