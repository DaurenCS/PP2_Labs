x=int(input())
a=[]

for i in range(0,x):
    s=int(input())
    a.append(s)
for i in range(len(a)):
    
    if a[i]<=10:
        print('Go to work!')
    elif a[i]>10 and a[i]<=25:
        print('You are weak')
    elif a[i]>25 and a[i]<=45:
        print('Okay, fine')
    elif a[i]>45:
        print('Burn! Burn! Burn Young!')
        
        

        
        
