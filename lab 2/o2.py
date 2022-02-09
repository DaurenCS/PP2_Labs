a,b=input().split('+')
arr=[]
arr2=[]
for i in range(len(a)//3):
    arr.append(a[i*3:3*i+3])
for i in range(len(b)//3):
    arr2.append(b[i*3:3*i+3])

def f(list):
    for i in range(len(list)):
        if list[i]=="ONE":
            list[i]=1
        if list[i]=="TWO":
            list[i]=2
        if list[i]=="THR":
            list[i]=3
        if list[i]=="FOU":
            list[i]=4
        if list[i]=="FIV":
            list[i]=5
        if list[i]=="SIX":
            list[i]=6
        if list[i]=="SEV":
            list[i]=7
        if list[i]=="EIG":
            list[i]=8
        if list[i]=="NIN":
            list[i]=9
        if list[i]=="ZER":
            list[i]=0       
f(arr)
f(arr2)
sum1=[]
def sum(list,l2,l3): 
    s=0
    s1=0
    for i in range(len(list)):
        s+=int(list[i])*pow(10,len(list)-1-i)
    for j in range(len(l2)):
        s1+=int(l2[j])*pow(10,len(l2)-1-j)
    sum1.append(s+s1)
sum(arr,arr2,sum1)
str=[str(w) for w in sum1]

out=[]
def f2(list,l2):
    for i in range(len(list[0])):
        if list[0][i]=='1':
            l2.append('ONE')
        if list[0][i]=="2":
            l2.append('TWO')
        if list[0][i]=="3":
            l2.append('THR')
        if list[0][i]=="4":
            l2.append('FOU')
        if list[0][i]=='5':
            l2.append('FIV')
        if list[0][i]=="6":
            l2.append('SIX')
        if list[0][i]=='7':
            l2.append('SEV')
        if list[0][i]=="8":
            l2.append('EIG')
        if list[0][i]=='9':
            l2.append('NIN')
        if list[0][i]=='0':
            l2.append('ZER')
f2(str,out)
for i in range(len(out)):
    print(out[i],end='')

