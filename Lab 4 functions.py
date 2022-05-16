def numbers(my_number:int = 5):
    '''
        Printing numbers in a hierarchical descending order
                      with defult value = 5
    '''
    for i in range(my_number, 0, -1):
        for j in range(i, 0,-1):
            print(j, end=" ")    
        print(" ")
print(numbers.__doc__)
numbers()
numbers(int(input("enter any number: ")))