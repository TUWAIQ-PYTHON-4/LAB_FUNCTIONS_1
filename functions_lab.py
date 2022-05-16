

def number_pattren(number: int)-> int:
    ''' This function takes a number and prints it in descending order shaped in a pyramid'''
    number = number
    for i in range(0, number):
     for j in range(number, i, -1):
         print(j, end=" ")
     print("\n")


number_pattren(5)
