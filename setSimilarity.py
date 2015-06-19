def sim(A, B):
	return len(set(A)&set(B))*1./len(set(A+B))
print sim([1, 2, 4, 6, 7],[2, 3, 4, 7])