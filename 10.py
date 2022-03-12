import re
def find(text):
	f = re.findall(r'[A-Za-z][a-z]+',text)
	f = [x.lower() for x in f]
	text = '_'.join(f)
	print(text)


find("AdsdSdsAds")
