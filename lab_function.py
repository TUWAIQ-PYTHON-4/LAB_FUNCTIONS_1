def numbers(num:int)->int:
    '''This function return reseve pattern ''' 
    for i in range(0,num):    
     for j in range(num,0,-1):   
         print(j, end=' ') 
     print(" ") 
     num-=1
print(numbers.__doc__)    
       
numbers(5)   
