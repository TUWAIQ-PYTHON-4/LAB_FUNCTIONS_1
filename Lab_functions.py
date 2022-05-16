# LAB_FUNCTIONS_1


## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):

def reverse_print(number:int):
    for i in range(number,0,-1):
        for j in range(i,0,-1):
            print(j, end= " ")
        print()

### Document the newly created function. describe what it does, then print the documentation. 

reverse_print(5)