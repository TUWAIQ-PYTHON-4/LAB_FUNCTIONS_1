def numbers(my_number:int = 5):
    for i in range(my_number, 0, -1):
        for j in range(i, 0,-1):
            print(j, end=" ")    
        print(" ")
numbers()
numbers(int(input("enter any number: ")))