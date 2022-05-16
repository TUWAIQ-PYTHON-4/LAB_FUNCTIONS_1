

def repeat(my_number:int): 
   for i in range(my_number,0, -1):
        for j in range(i,0,-1):
          print(j, end=" ")  
          print(" ")
        repeat(9)
# print(repeat.__doc__)
help(repeat)