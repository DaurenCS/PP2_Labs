import os

path = "C:/Users/ASus/Desktop/KBTU/pp2 labs/lab6/direct"
del_f = "file2.txt"
for  i in os.listdir(path):
	if i == del_f:
		os.remove(i)


