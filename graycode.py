def bin2gray(bits):
	bits = int(''.join(str(n) for n in bits),2)
	res = (bits >> 1) ^ bits
	return map(int,list(bin(res)[2:]))
def gray2bin(bits):
	bits = int(''.join(str(n) for n in bits),2)
	m = bits>>1
	while m!=0:
		bits = bits^m
		m=m>>1
	return map(int,list(bin(bits)[2:]))

print(bin2gray([1,0]))
print(gray2bin([1,1,0]))
