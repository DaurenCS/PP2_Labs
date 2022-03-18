import os

path = os.getcwd()

f = os.access(path, os.F_OK)
r = os.access(path, os.R_OK)
w = os.access(path, os.W_OK)
x = os.access(path, os.X_OK)
print(f'{path} :{f}')
print(f'{path} :{r}')
print(f'{path} :{w}')
print(f'{path} :{x}')
