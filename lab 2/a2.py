x=input().split()

arr=[]
for i in range(len(x)):
    if '0' not in x:
        print(1)
        exit(0)
        
    elif x[i]=='0':
        arr.append(i)
arr2=[]
for j in range(len(arr)):
    cont=0
    for i in range(len(x)):
        if int(x[i])>arr[j]-i and arr[j]>=i:
            cont+=1
    arr2.append(cont)



if 0 in arr2 and int(x[-1])!=0:
    print(0)
    
else:
    print(1)
    
    
        


