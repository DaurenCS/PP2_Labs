import re 
x=input()
a = re.sub(r'[^\w\s]','', x)


arr=a.split()
arr.sort()
arr2=[]
for i in arr:
    if i not in arr2:
        arr2.append(i)

    
print(len(arr2))
for i in range(len(arr2)):
    print(arr2[i])
    



  



