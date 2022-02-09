arr=[]
while True:
    
    x=input()
    t=x.split(" ")
    
    arr.append(t)
    if x=='0':
        arr.remove(t)
        break
arr.sort(key =lambda a:(a[2],a[1],a[0]))
for i in range(len(arr)):
    print(arr[i][0],arr[i][1],arr[i][2])
    


    
