import os

list_upper = list(map(chr, range(65, 91)))

for i in list_upper:
	f = open(f'{i}.txt', "x" )