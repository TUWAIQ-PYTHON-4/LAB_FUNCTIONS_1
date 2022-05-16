def numbers_print_function():
    '''
    1- ask the user number 
    2- understan rows and columes 
    3- create first'for loop' to handle number of rows [outer loop]
    4- create second 'for looop' to handle number of columns[nested loop], here [-1] it's mean start from the last عشان تكون بالعافيه 
    '''
    user_input=int(input("Enter the number you want :"))
    for i in range(0 , user_input ):
        for j in range(user_input ,i, -1):
            print(j,end=' ')
        print()

numbers_print_function()