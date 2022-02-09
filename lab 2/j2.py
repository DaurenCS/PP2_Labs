x= int(input())
arr=set()
for i in range(x):
    a=input()
    arr.add(a)

arr=list(arr)
arr.sort()
cont=0
arr2=[]
for i in range(len(arr)):
    if not arr[i].islower() and not arr[i].isupper() and not arr[i].isdigit() and not arr[i].isalpha():
        cont+=1
        arr2.append(arr[i])
        
        
print(cont)
for i in range(len(arr2)):
    print(arr2[i])
