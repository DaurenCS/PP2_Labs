x=str(input())
a=str(input())

arr=[]

for i in range(0,len(x)):
    if x[i]==a:
        arr.append(i)
        
if len(arr)>1:
    print(arr[0],arr[-1])
elif len(arr)==1:
    print(arr[0])
