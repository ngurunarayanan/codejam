import sys
import math

T = int(sys.stdin.readline().strip())

for i in xrange(1, T+1):
	N, K = map(int, sys.stdin.readline().strip().split())
	cakes = []
	for j in xrange(N):
		r, h = map(float, sys.stdin.readline().strip().split())
		cakes.append([r*r*math.pi, 2*r*h*math.pi])
	ans = sorted(cakes, key=lambda x : x[1], reverse=True)[0:K-1]
	rem = sorted(cakes, key=lambda x : x[1], reverse=True)[K-1:]
	ans = sorted(ans, key=lambda x : x[0], reverse=True)
	total = 0 if len(ans) == 0 else ans[0][0]
	base_area = total
	for j in ans:
		total += j[1]
	cur_dif = 0
	max_dif = 0
	for j in xrange(len(rem)):
		if rem[j][0] > base_area:
			cur_dif = rem[j][0] - base_area + rem[j][1]
		else:
			cur_dif = rem[j][1]
		if cur_dif > max_dif:
			max_dif = cur_dif
	total += max_dif
	print "Case #" + str(i) + ": %.9f" % total

