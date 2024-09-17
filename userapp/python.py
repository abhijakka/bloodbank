a=8
for i in range(a):
    print(' '*(a-i-1),end='')
    for j in range(i+1):
        print(' ',i+1,end='')
    print()    
for j in range(a-1):
    print(' '*(j+1),end='')
    for i in range(a-j-1):
        print(' ',i+1,end='') 
    print()           
    


