import re

def find(text):
	p = r'a.*'
	if re.search(p, text):
		print("YES")
	else:
		print("NO")
find('babb')

