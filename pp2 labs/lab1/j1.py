x = str(input())
arr=[]
arr= x.split(" ")
for i in range(0, len(arr)):
    if len(arr[i])>=3:
        print(arr[i], end=' ')
    else:
        continue
