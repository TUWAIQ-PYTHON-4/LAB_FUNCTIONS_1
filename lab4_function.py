
def pattren_number(number:int)-> int:
    '''
    function that takes 1 parameter of type int , then it prints out the result formatted like the following patter
    (if we give it 5 for example):
        5 4 3 2 1   
        4 3 2 1   
        3 2 1   
        2 1   
        1   
    '''
rows = 5
for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print(j, end=' ')
    print(" ")

pattren_number(5)
print(pattren_number.__doc__)