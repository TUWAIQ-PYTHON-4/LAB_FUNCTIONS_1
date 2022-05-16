# Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example): from traceback import print_last


def print_full_numbers(number:int=5):
    """
        This is function takes 1 parameter of type int , then it prints out the result formatted like the following patter 
    """

    for i in range(0,number):
        for j in range(number, 0,-1):
            print(j, end=" ")
        number -=1
        
        print("")

print_full_numbers(6)

#Document the newly created function. describe what it does, then print the documentation.
print(print_full_numbers.__doc__)

