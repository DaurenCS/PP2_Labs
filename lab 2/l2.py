x=input()

arr=[]

for i in x:
    if len(arr)==0:
        arr.append(i)
        if arr[0]=='}' or arr[0]==']' or arr[0]==')':
            print('No')
            exit(0)
    elif len(arr)!=0:
        if arr[-1]=='[' and i==']' or arr[-1]=='{' and i=='}' or arr[-1]=='(' and i==')':
            arr.pop()
        else:
            arr.append(i)
            
            
        
    

if len(arr)==0:
    print('Yes')
else:
    print('No')
    

    

