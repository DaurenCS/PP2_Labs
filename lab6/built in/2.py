def count(text):
    CNT = 0
    cnt = 0
    for i in range(len(text)):
        if text[i].islower():
            cnt+=1
        else:
            CNT+=1
    print("Lower case leter :",cnt, end= '\n')
    print("Upper case letter :", CNT)
count("ASDqwer")