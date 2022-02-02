import math
x= int(input())
a=input()

if a=='k':
    b=str(input())
    s='{0:.'+b+'f}'
    
    x=x/1024
    print(s.format(x))
else:
    print(x*1024)
