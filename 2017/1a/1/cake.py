import sys

T = int(sys.stdin.readline())

for i in xrange(1, T+1):
	r, c = map(int, sys.stdin.readline().strip().split())
	cake = []
	for j in xrange(r):
		cake.append(list(sys.stdin.readline().strip()))
		for k in xrange(1, c):
			if cake[j][k] == '?':
				cake[j][k] = cake[j][k-1]
		for k in xrange(c-2, -1, -1):
			if cake[j][k] == '?':
				cake[j][k] = cake[j][k+1]
		if j:
			if cake[j][0] == '?':
				for k in xrange(c):
					cake[j][k] = cake[j-1][k]
	for j in xrange(r-2, -1, -1):
		if cake[j][0] == '?':
			for k in xrange(c):
				cake[j][k] = cake[j+1][k]
	print "Case #" + str(i) + ":"
	for j in range(r):
		print ''.join(cake[j])
		
