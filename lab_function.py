def numbers(num:int)->int:
    '''This function return the reseve pattren''' 
    for i in range(num + 1, 1, -1):    
     for j in range(1, i - 1):  
        print(j, end=' ')  
     print(" ")  

numbers(6)    
