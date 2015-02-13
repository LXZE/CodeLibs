def justify(text, width):
	temp = ''
	res = []
	for word in text.split(' '):
		if len(word)+(len(temp)-1) < width:
			temp += '%s '% word
		else:
			res.append(temp[:-1])
			temp = '%s '% word
	res.append(temp[:-1])
	t = res
	res = []
	for s in t[:-1]:
		sCount = s.count(' ')
		if sCount != 0 :
			index = [1]*sCount
			init = list(index)
			left = width-len(s)
			i = 0
			while sum(index)-sum(init) < left:
				if i == sCount: i = 0
				index[i]+=1
				i+=1
			index.append(0)
			sp = s.split(' ')
			r = ''
			for i in range(0,len(sp)):
				r+=sp[i]+(' '*index[i])
			res.append(r)
		else : res.append(s)
	res.append(t[-1])
	return '\n'.join(res)
arr = justify(raw_input(),input())
for line in arr.split('\n'):
	print line,len(line)