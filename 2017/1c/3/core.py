import sys

T = int(sys.stdin.readline().strip())

for C in xrange(1, T+1):
	n, k = map(int, sys.stdin.readline().strip().split())
	u = float(sys.stdin.readline().strip())
	p = map(float, sys.stdin.readline().strip().split())
	p.sort()
	p.append(1.0)
#	print p
	for i in xrange(n):
		diff = p[i+1] - p[i]
		required = diff * (i+1)	
		if required <= u:
			u = u-required
			for j in xrange(i+1):
				p[j] = p[i+1]
		else:
			add = u / float(i+1)
			for j in xrange(i+1):
				p[j] += add
			u = 0
			break
	prod = 1
#	print p
	for i in xrange(n):
		prod = prod * p[i]
	print "Case #{}: {:.6f}".format(C, prod)
