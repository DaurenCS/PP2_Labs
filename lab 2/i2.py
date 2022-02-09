x=int(input())
arr=[]
for i in range(x):
    a=input()
    t=a.split(" ")
    arr.append(t)
arr2=[]
arr3=[]
arr.reverse()
for i in range(len(arr)):
    if arr[len(arr)-1-i][0]=='1':
        arr2.append(arr[len(arr)-1-i][1])
        
    else:
        arr3.append(arr2[0])
        arr2.remove(arr2[0])

for i in range(len(arr3)):
    print(arr3[i],end=' ')
        
    
