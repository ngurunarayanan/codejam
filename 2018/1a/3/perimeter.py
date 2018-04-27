import sys
import math

T = int(sys.stdin.readline().strip())

for C in xrange(1, T+1):
	n, p = map(int, sys.stdin.readline().strip().split())
	ws = []
	hs = []
	w = 0
	h = 0
	for i in xrange(n):
		w, h = map(int, sys.stdin.readline().strip().split())
		ws.append(w)
		hs.append(h)
	l = 2*min(w, h)
	r = 2*math.sqrt((w*w) + (h*h))
	ps = n * 2 * (w + h)
	pd = p - ps
	if pd == 0:
		print "Case #{}: {}".format(C, p)
		continue
	for i in xrange(1, n+1):
		L = i*l
		R = i*r
		if pd >= L and pd <= R:
			print "Case #{}: {}".format(C, p)
			break
		elif pd > R:
			continue
		else:
			print "Case #{}: {}".format(C, ps + (i-1)*r)
			break
	else:
		print "Case #{}: {}".format(C, ps + (n)*r)


