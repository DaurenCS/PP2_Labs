import re
def find(text):
	p = re.sub( "\W",":",text )
	print(p)
find("s dA,asdb")
find("aA*s bd asd")
find("AA'As asb")