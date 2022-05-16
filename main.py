



def number(rows= int):
  '''
  this function order number in trangale 
  '''
for i in range(0,rows+ 1):    
    for j in range( rows - i , 0 , -1):  
        print(j, end=' ')  
    print()  

number(5)
