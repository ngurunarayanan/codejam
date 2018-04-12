import sys

def lcm (x, y):
	n = max(x, y)
	m = min(x, y)
	rem = n % m
	i = 1
	while rem > 0:
		i += 1
		rem = (n * i) % m
	return n * i
		
		
T = int(sys.stdin.readline().strip())

for C in xrange(1, T+1):
	b, n = map(int, sys.stdin.readline().strip().split())
	m = map(int, sys.stdin.readline().strip().split())
	l = reduce(lcm, m)
	s = 0
	for i in m:
		s += l / i 
	N = n % s
	if N == 0:
		N = s
	t = [0 for i in xrange(b)]
	#print "l = {}, s = {}, n = {}".format(l, s, N)
	min_id = 0
	for i in xrange(N):
		min_id = 0
		min_ele = t[0]
		for j in xrange(1, b):
			if t[j] < min_ele:
				min_ele = t[j]
				min_id = j
		t[min_id] += m[min_id]
	print "Case #{}: {}".format(C, min_id + 1)
			
	

		
