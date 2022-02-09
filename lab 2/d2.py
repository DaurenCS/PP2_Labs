x=int(input())

if x%2!=0:
    for i in range(x):
        for j in range(x):
            if i+j<x-1:
                print('.',end='')
            else:
                print('#',end='')
                
            
        print(end='\n')
if x%2==0:
    for i in range(x):
        for j in range(x):
            if  i<j:
                print('.',end='')
            else:
                print('#',end='')
                
            
        print(end='\n')

