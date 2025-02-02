import string
import re

text = open('text.txt','r').read().lower()
flag = open('flag.txt','r').read().strip()[4:-1].replace('_','+')
chars = string.ascii_letters + string.digits + '+/='
regex = re.compile('[' + chars + ']{5,70}')
assert re.fullmatch(regex, flag)

def caesar(msg, shift):
	return ''.join(chars[(chars.index(c) + shift) % len(chars)] for c in msg)

i = 0
count = 0
while i < len(text):
	if text[i] not in string.ascii_lowercase:
		print(text[i], end = '')
		i += 1
	else:
		j = i
		while text[j] in string.ascii_lowercase: j += 1
		print(caesar(text[i:j], chars.index(flag[count % len(flag)])), end = '')
		count += 1
		i = j

