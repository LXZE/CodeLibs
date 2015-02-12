def intToroman(n):
	val = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC')
	,(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
	str = ''
	for v in val:
		while n>=v[0]:
			n-=v[0]
			str+=v[1]
	return str
print(intToroman(2014))