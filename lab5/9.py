import re
arr = []
def find(text):
	p = re.findall(r'[A-Z][a-z]+',text)
	for i in range(len(p)):
		print(p[i], end=' ')
	 

find("AsdfdgASdFdf")

