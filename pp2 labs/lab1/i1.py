x=int(input())
s=[]
arr=[]
for i in range(0,x):
    a=str(input())
    s.append(a)

for i in range(0, len(s)):
    if "@gmail.com" in s[i]:
        print(s[i][0:len(s[i])-10])

