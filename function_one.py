'''
Create a function that takes 1 parameter of type int , 
then it prints out the result formatted like 
the following pattern (if we give it 5 for example):

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

Document the newly created function.
describe what it does,
then print the documentation.
'''

# defining the function.
def pyramid_numbers(num: int):
    '''
    this function takes one number as integer,
    and prints it in a pattern like pyramid in a specific pattern.
    '''
    while num != 0:
        for item in range(num,0,-1):
           print(item, end=" ")
        print(" ")
        num-= 1
# calling the function
pyramid_numbers(5)
# printing documentation
print(pyramid_numbers.__doc__) 