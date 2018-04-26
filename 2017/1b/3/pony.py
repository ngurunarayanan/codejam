import sys

def fastest(n, cpos, cpe, cps, speed, energy, distance, ht):
	if cpos == n-1:
		return 0
	if ht.has_key((cpos, cpe, cps)):
		return ht[cpos, cpe, cps]
	m1 = 0xffffffffffffffff
	m2 = 0xffffffffffffffff
	if cpe >= distance[cpos]:
		m1 = distance[cpos]/cps + fastest(n, cpos+1, cpe-distance[cpos], cps, speed, energy, distance, ht)
	if energy[cpos] >= distance[cpos]:
		m2 = distance[cpos]/speed[cpos] + fastest(n, cpos+1, energy[cpos]-distance[cpos], speed[cpos], speed, energy, distance, ht)

	#print n, cpos, cpe, cps, speed, energy, distance, m1, m2
	ht[cpos, cpe, cps] = min(m1, m2)
	return min(m1, m2)


T = int(sys.stdin.readline())



for C in xrange(1, T+1):
	N, Q = map(int, sys.stdin.readline().strip().split())
	speed = []
	energy = [] 
	for i in xrange(N):
		e, s = map(float, sys.stdin.readline().strip().split())
		speed.append(s)
		energy.append(e)
	distances = []
	dist = []
	for i in xrange(N):
		row = map(float, sys.stdin.readline().strip().split())
		distances.append(row)
	for i in xrange(N-1):
		dist.append(distances[i][i+1])

	us = []
	vs = []
	for i in xrange(Q):
		u, v = map(int, sys.stdin.readline().strip().split())
		us.append(u)
		vs.append(v)
	time = fastest(N, 0, 0, 0, speed, energy, dist, {})
	print "Case #{}: {:.6f}".format(C, time)
