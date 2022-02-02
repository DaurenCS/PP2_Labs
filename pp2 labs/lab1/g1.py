x=str(input())
sum=0
for i in range(0,len(x)) :
    
    sum=sum+int(x[i])*(2**(len(x)-1-i))
    
print(sum)
    

