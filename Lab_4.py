
def digital_pyramid(num:int = 5):
    '''
    This function takes the number and repeats it through For Loop 
    and every time it decreases a number and builds these numbers in an inverse hierarchical form
    '''
    while num > 0:
     
     for i in range(num,0,-1):
        
            print (i, end=' ')
     num -= 1      
     print('')
  
        
         
digital_pyramid(10)  

print(digital_pyramid.__doc__)








