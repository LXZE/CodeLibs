def snail(array):
	startx,starty = 0,0; edgex = len(array[0])-1; edgey = len(array)-1
	res = []
	while startx < edgex and starty < edgey:
		for i in range(startx,edgex):
			res.append(array[startx][i])
		for i in range(starty,edgey):
			res.append(array[i][edgey])
		for i in range(edgex,startx,-1):
			res.append(array[edgex][i])
		for i in range(edgey,starty,-1):
			res.append(array[i][starty])
		startx+=1; starty+=1; edgex-=1; edgey-=1;
		# print(res)
	if len(array)%2 != 0:
		mid = (len(array)/2)
		res.append(array[mid][mid])
	return res
array = [[1,2,3,4],
         [12,13,14,5],
         [11,16,15,6],
         [10,9,8,7]]
print(snail(array))
array = [[1,2,3,4,5],
		[16,17,18,19,6],
		[15,24,25,20,7],
		[14,23,22,21,8],
		[13,12,11,10,9]]
print(snail(array))
array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
print(snail(array))
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
print(snail(array))
array = [[1,2],[4,3]]
print(snail(array))
