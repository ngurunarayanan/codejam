import sys

T = int(sys.stdin.readline().strip())
for X in xrange(1, T+1):
	N, C, M = map(int, sys.stdin.readline().strip().split())
	c_arr = [[] for i in xrange(C)]
	for i in xrange(M):
		p, c = map(int, sys.stdin.readline().strip().split())
		c_arr[c-1].append(p)
	for i in xrange(C):
		c_arr[i].sort()
	count = 0
	n1 = len(c_arr[0])
	n2 = len(c_arr[1])
	i = 0
	min_req = 0
	min_prom = 0
	if n1 == 0 or n2 == 0:
		min_req = max(n1, n2) 
		print "Case #{}: {} {}".format(X, min_req, min_prom)
		continue
	i = 0
	while i < n1:
		j = 0
		while i < n1 and j < n2: 
			if c_arr[0][i] < c_arr[1][j]:
				c_arr[0].pop(i)
				c_arr[1].pop(j)
				n1 -= 1
				n2 -= 1
				min_req += 1
				continue
			j += 1
		i += 1
			
	i = 0
	while i < n2:
		j = 0
		while i < n2 and j < n1: 
			if c_arr[1][i] < c_arr[0][j]:
				c_arr[1].pop(i)
				c_arr[0].pop(j)
				n1 -= 1
				n2 -= 1
				min_req += 1
				continue
			j += 1
		i += 1
	#print c_arr[0], c_arr[1]
	if n1 and n2 and c_arr[0][0] != 1:
		min_req += min(n1, n2) + abs(n1 - n2)
		min_prom = min(n1, n2)
	elif n1 and n2:	
		min_req += n1 + n2
	else:
		min_req += max(n1, n2)
		
	print "Case #{}: {} {}".format(X, min_req, min_prom)
