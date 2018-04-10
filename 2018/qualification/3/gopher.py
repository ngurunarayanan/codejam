import sys

T = int(sys.stdin.readline())

for i in xrange(T):
	A = int(sys.stdin.readline())
	rect = [0 for j in range(A+2)]
	done = False
	j = 2
	out = [[0 for j in xrange(11)] for k in xrange(11)]
	r = 2
	c = 2
	e = 0
#	sys.stderr.write(str(out))
	while not done:
		print r, c
		sys.stdout.flush()
		nr, nc = map(int, sys.stdin.readline().split())
		if nr == 0 and nc == 0:
			break
		if nr == -1 or nc == -1:
			e = 1
			break	
#		sys.stderr.write("\n"+str(nr) + ":"+str(nc))
		out[nr][nc] = 1
		c += 1
		if c == 7:
			c = 2
			r += 1
		if r == 5:
			r = 2
			c = 2
			
	if e == 1:
		break	
