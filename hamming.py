def hamming(n):
	h = 1;_h=[1]
	base  = (2, 3, 5)
	selected  = [0 for i in base]
	val = [x * _h[i] for x,i in zip(base, selected)]
	for i in range(1,n):
	    h = min(val)
	    _h.append(h)
	    for (n,(v,x,i)) in enumerate(zip(val, base, selected)):
	        if v == h:
	            i += 1
	            selected[n] = i
	            val[n] = x * _h[i]
	    mini = min(selected)
	    if mini >= 1000:
	        del _h[:mini]
	        selected = [i - mini for i in selected]
	return h