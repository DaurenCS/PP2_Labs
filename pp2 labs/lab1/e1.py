def f(x):
    for i in range(2,x//2):
        if x%i==0:
             return 0
    return 1
a, b = [int(a) for a in input().split()]
if f(a) and a<500 and b%2==0:
    print('Good job!')
else:
    print('Try next time!')
            
             

