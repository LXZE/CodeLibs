def convert(input, source, target):
	if source == target:
		return input
	base = {
		'bin' :'01',
		'oct' :'01234567',
		'dec' :'0123456789',
		'hex' :'0123456789abcdef',
		'allow' :'abcdefghijklmnopqrstuvwxyz',
		'allup' :'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
		'alpha' :'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
		'alphanum' :'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		}
	baseSrcList = base[source]
	baseSrc = len(baseSrcList)
	baseTargetList = base[target]
	baseTarget = len(baseTargetList)
	
	# convert input base[source] to base[10]
	data = 0
	if baseSrc != 10:
		i = 0
		for iDigit in list(str(input)[::-1]):
			data += baseSrcList.index(iDigit)*pow(baseSrc,i)
			i+=1
	else : data = input

	# convert data base[10] to base[target]
	if baseTarget != 10:
		tempInput = int(data)
		t = ''
		if tempInput == 0: t+=baseTargetList[0]
		while tempInput != 0:
			t += baseTargetList[tempInput%baseTarget]
			tempInput/=baseTarget
		return t[::-1]
	else:
		return str(data)



print(convert('16','dec','hex')  == '10')
print(convert('15', 'dec', 'bin') == '1111')
print(convert('15', 'dec', 'oct') == '17')
print(convert('1010', 'bin', 'dec') == '10')
print(convert('1010', 'bin', 'hex') == 'a')
print(convert('0', 'dec', 'alpha') == 'a')
print(convert('27', 'dec', 'allow') == 'bb')
print(convert('hello', 'allow', 'hex') == '320048')
print(convert('SAME', 'alup', 'alup') == 'SAME')