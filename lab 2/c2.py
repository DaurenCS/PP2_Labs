x=int(input())

for i in range(x):
   
    for j in range(x):
        if j==0:
            print(i,end=' ')
            
        elif i==0:
            print(j,end=' ')
        elif i==j:
            print(j*j,end=' ')

        else:
            print(0,end=' ')
        
       
        
         

    print(end='\n')
         

    
