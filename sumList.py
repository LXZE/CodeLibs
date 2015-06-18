def sum_for_list(list):
	def primes(n):
		sieve = [True] * n
		for i in xrange(3,int(n**0.5)+1,2):
			if sieve[i]: sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
		return [2] + [i for i in xrange(3,n,2) if sieve[i]]
	plist = primes(max(map(lambda x:abs(x),list)))
	res = []
	for p in plist:
		pa = filter(lambda x: x%p==0,list)
		if pa != []: res.append([p,sum(pa)])
	return res

a = [12, 15]
# sum_for_list(a)
print sum_for_list(a) == [[2, 12], [3, 27], [5, 15]]