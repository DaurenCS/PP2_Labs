import math
x=input().split()

a=int(input())
arr=[]


for i in range(a):
    s=input().split()
    sum=float(math.sqrt(pow((int(s[0])-int(x[0])),2)+pow((int(s[1])-int(x[1])),2)))
    
    arr.append((sum,s))

    
arr.sort()

for i in range(a):
    print(arr[i][1][0],arr[i][1][1])
