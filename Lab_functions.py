# LAB_FUNCTIONS_1


## Create a function that takes 1 parameter of type int , 
## then it prints out the result formatted like the following pattern (if we give it 5 for example):

def reversed_print(number:int):
    '''
    The reversed_print function take a number as an argument and then prints out the result in the following format 
    examply: number = 3 
    The result:
    3 2 1 
    2 1 
    1
    '''
    for i in range(number,0,-1):
        for j in range(i,0,-1):
            print(j, end= " ")
        print()

reversed_print(5)
### Document the newly created function. describe what it does, then print the documentation. 
help(reversed_print)
