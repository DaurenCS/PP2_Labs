import re
def find(text):
	pattern = r'[A-Z]{1}[a-z]*'
	print(*re.findall(pattern, text)) 	
find("sdaAsdb")
find("asAdAsd")
find("AaAsasb")