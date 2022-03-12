import re
def find(text):
	p = r'[A-Z]+[a-z]+'
	if re.search(p, text):
		print("Yes")

	else:
		print("NO")
find("sdAasd")
find("Asdasd")
find("AAA")