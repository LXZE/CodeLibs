import random as r
fx = lambda weight,inNode,delta: 1 if reduce(lambda x,y: x+y, [ x*y for x,y in zip(weight,inNode) ])-delta >= 0 else 0
inputSet = [ # n column data set with m row
[0,0,0],
[0,0,1],
[0,1,0],
[0,1,1],
[1,0,0],
[1,0,1],
[1,1,0],
[1,1,1]
]
outputSet = [0, 0, 0, 0, 0, 0, 0, 1 ] # expected output of each row
weight = [round(r.uniform(-5,5), 1) for i in range(0,3)] # random weight n values from -5 to 5
delta = 1
a = 0.2
epoch = 1
while True:
	count = 0
	for i,inVal in enumerate(inputSet):
		err = outputSet[i] - fx(inVal,weight,delta)
		if err != 0:
			count+=1
			for j,val in enumerate(inVal):
				if val!= 0 : 
					weight[j] += a*err*val
			delta += -a*err
		for j,w in enumerate(weight):
			weight[j] = round(w,3) # round num
		print 'Input:{}, Weight={}, Error={}'.format(inputSet[i],weight, err)
	print 'Epoch {}: weight={}, delta={}'.format(epoch,weight,delta) 
	epoch+=1
	if count == 0:
		break