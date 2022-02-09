arr=[]
while True:
    x=int(input())
    arr.append(x)
    if x==0:
        arr.remove(x)
        break
arr3=[]
if len(arr)%2==0:
    for i in range((len(arr)//2)):
        sum=arr[i]+arr[-1-i]
        arr3.append(sum)
else:
    for i in range((len(arr)//2)):
        sum=arr[i]+arr[-1-i]
        arr3.append(sum)
    arr3.append(arr[len(arr)//2])
    

for i in range(len(arr3)):
    print(arr3[i],end=' ')
    
