import math 
def pal(text):
    cont = 0
    for i in range(len(text)//2):
        if text[i] == text[-1-i]:
            cont += 1
    
    if cont == math.ceil(len(text)//2):
        print("YES")
    else:
        print("NO")
    
pal("asddsddsa")