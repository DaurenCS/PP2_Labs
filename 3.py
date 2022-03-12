import re
def find(text):
    p = r'^[\w]+_[\w]'
    if re.search(p, text):
        return 'Yes'
    else:
        return 'No'
print(find('a_b'))
print(find('ab'))
print(find('aa_sdv'))
print(find('asasd_'))