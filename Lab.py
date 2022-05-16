def hierarchical_pattern(number:int):
 ''' function that takes 1 parameter of type int , 
 then it prints out the result hirarchical pattern.
     '''
 for i in range(number,-number,-1):
    for j in range(i,0,-1):
        # display number
        print(j, end=' ')
    # new line after each row
    print('')
hierarchical_pattern(5)
print(hierarchical_pattern.__doc__)