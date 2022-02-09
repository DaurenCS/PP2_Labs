n = int(input())
dic = dict()
for i in range(n):
    name,pay = map(str,input().split())
    
    if name in dic:
        
        dic[name] = dic[name] + int(pay)
        
        
        
    else:
        dic[name] = int(pay)

l = dic.values()
maax = max(l)
for key,value in sorted(dic.items()):
    if int(value)==maax:
        print(f'{key} is lucky!')
    else:
        print(f'{key} has to receive {maax-int(value)} tenge')
