import re
def find(text):
        patterns = r'a[b]{2,3}'
        if re.search(patterns,  text):
                return 'Yes'
        else:
                return('No')
print(find('abb'))
print(find('babb'))
print(find('abbbbbbbb'))
print(find('asm'))