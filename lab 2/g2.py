x=int(input())

d=dict()

for i in range(x):
    k,v=input().split()
    if v in d:
        d[v]+=1
    else:
        d[v]=1
y=int(input())

for i in range(y):
    a,b,c=input().split()
    if b in d:
        if d[b]>=int(c):
            d[b]-=int(c)
        elif d[b]<int(c):
            d[b]=0
sum=0
for i in d:
    sum+=int(d[i])
print('Demons left:',sum)
    
