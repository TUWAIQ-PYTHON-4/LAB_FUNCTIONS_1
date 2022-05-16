def num(number:int):
 '''we defined a function that print the numbers backwords'''    

 for i in range(number):
     
    
    for j in range(number,0,-1):
        
        print(j, end=' ')
    
    print('')
    number-=1




'''def num(x:int):
 for i in range(1, x):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print("")'''

num(5)
print(num.__doc__)