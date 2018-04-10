import sys

T = int(sys.stdin.readline().strip())

for i in xrange(1, T+1):
	D, N = map(int, sys.stdin.readline().strip().split())
	K = [0 for j in xrange(N)]
	S = [0 for j in xrange(N)]
	for j in xrange(N):
		K[j], S[j] = map(float, sys.stdin.readline().strip().split())
	Times = map(lambda x, y: (D-x)/y, K, S)
	max_time = reduce(lambda x, y:  x if x > y else y, Times)
	print "Case #" + str(i) + ": " + str(float(D) / max_time)

