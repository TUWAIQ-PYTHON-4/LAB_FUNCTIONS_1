
'''
## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):

5 4 3 2 1   
4 3 2 1   
3 2 1   
2 1   
1   

### Document the newly created function. describe what it does, then print the documentation. 
'''

def pyramidal(number):
    '''
    this method will print numbers like shape pyramidal 
    '''
    for first_loop in range(1,number+1):
        num=number
        for secand_loop in range(number,first_loop-1,-1):
            print(secand_loop, end=' ')
        print()
pyramidal(5)
print(pyramidal.__doc__)

