x=2
n=[int(x) for x in input().split()]
if len(n)==1:
        b=int(input())
        n.append(b)
a=[]

for i in range(n[0]):
        s=n[-1]+2*i
        a.append(s)
sum=a[0]        
for i in range(1,len(a)):
        sum^=a[i]
print(sum)
     







