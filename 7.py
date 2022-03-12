import re
def find(text):
	new_string="" 
	for i in range(len(text)):
		if text[i]=='_':
			 new_string+=text[i+1].upper()
		elif text[i]!="_" and text[i-1]=="_":
			continue

		else: 
		     new_string+=text[i]

	p = re.sub( r'_[a-z]?',"",new_string )
	print(p)
find("s_da_sdb")
find("a_s_Ad_asd")
find("Aa_As_asb")