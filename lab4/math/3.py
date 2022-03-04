import math
n = int(input())
l = int(input())

s = (n*pow(l,2))/(4*math.tan(math.radians(180/n)))
print(int(s))