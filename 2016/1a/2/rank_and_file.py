import sys

T = int(sys.stdin.readline().strip())

for C in xrange(1, T+1):
	d = {}
	n = int(sys.stdin.readline().strip())
	slips = []
	for i in xrange(2*n - 1):
		slip = map(int, sys.stdin.readline().strip().split())
		for j in slip:
			if d.has_key(j):
				d[j] += 1
			else:
				d[j] = 1
		
		slips.append(slip)
	out = []
	for i in xrange(2*n - 1):
		for j in xrange(n):
			if d[slips[i][j]] % 2 != 0:
				out.append(slips[i][j])

	out.sort()
	out1 = []
	l = len(out)
	if l > 0:
		out1.append(out[0])
	for i in xrange(1, l):
		if out[i] != out[i-1]:
			out1.append(out[i])
	print "Case #{}: {}".format(C, ' '.join(map(str, out1)))
			
