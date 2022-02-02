x=str(input())

for i in x:
    ind=ord(i)
    if ind>=65 and ind<=90:
        ind+=32
    print(chr(ind),end='')
    


    
