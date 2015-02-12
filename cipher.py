import string
from codecs import encode as _dont_use_this_

def rot13(message):
	res = []
	list(message)
	for c in message:
		if ord('A') <= ord(c) and ord(c) <= ord('z'):
			tmp = ord(c) + 13
			if ord(c) < 91 and tmp > 90: tmp-=26
			elif tmp > 122 : tmp-=26
			res.append(chr(tmp))
		else: res.append(c)
	return string.join(res)
print(rot13(raw_input()))
#str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
#rot13(str)
