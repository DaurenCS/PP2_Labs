import re
def find(text):
	p = r'[\w]?a[a-z]+b$'
	if re.search(p, text):
		print("Yes")

	else:
		print("NO")
find("sdAasdb")
find("aAsbdasd")
find("AAAasb")