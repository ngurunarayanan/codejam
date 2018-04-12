import sys

T=int(sys.stdin.readline().strip())

for C in xrange(1, T+1):
	n = int(sys.stdin.readline().strip())
	ms = map(int, sys.stdin.readline().strip().split())
	m1 = 0
	for i in xrange(1, n):
		m1 += max(ms[i-1] - ms[i], 0)
	max_diff = 0
	for i in xrange(1, n):
		max_diff = max(max_diff, ms[i-1] - ms[i])
	m2 = 0
	for i in xrange(1, n):
		m2 += min(ms[i-1], max_diff)
	print "Case #" + str(C) + ":", m1, m2

