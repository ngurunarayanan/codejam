import sys

T = int(sys.stdin.readline().strip())

for C in xrange(1, T+1):
	r, c, h, v = map(int, sys.stdin.readline().strip().split())
	w = [[0 for i in xrange(c)] for j in xrange(r)]
	rsums = []
	for i in xrange(r):
		s = sys.stdin.readline().strip()
		rsums.append(0)
		for j in xrange(c):
			if s[j] == '@':
				w[i][j] = 1
				rsums[i] += 1
	#print w
	tot = sum(rsums)
	if tot % ((h + 1)*(v + 1)) != 0:
		print "Case #{}: IMPOSSIBLE".format(C)
		continue
	csums = []
	for i in xrange(c):
		csums.append(0)
		for j in xrange(r):
			if w[j][i] == 1:
				csums[i] += 1

	#print csums
	cur_sum = 0
	req_rsum = tot/(h+1)
	hlines = [0]
	exit = 0
	for i in xrange(r):
		cur_sum += rsums[i]
		if cur_sum == req_rsum:
			cur_sum = 0
			hlines.append(i+1)
		elif cur_sum > req_rsum:
			print "Case #{}: IMPOSSIBLE".format(C)
			exit = 1
			break
	if exit == 1:
		continue
	cur_sum = 0
	req_csum = tot/(v+1)
	vlines = [0]
	for i in xrange(c):
		cur_sum += csums[i]
		if cur_sum == req_csum:
			cur_sum = 0
			vlines.append(i+1)
		elif cur_sum > req_csum:
			print "Case #{}: IMPOSSIBLE".format(C)
			exit = 1
			break
	if exit == 1:
		continue
	
	#print hlines, vlines
	num_req = (h+1)*(v+1)
	sum_req = tot/num_req
	hsi = 0
	hei = 1
	for i in xrange(h+1):
		hs = hlines[hsi]
		he = hlines[hei]
		hsi += 1
		hei += 1
		vsi = 0
		vei = 1
		for j in xrange(v+1):
			vs = vlines[vsi]
			ve = vlines[vei]
			vsi += 1
			vei += 1
			cur_sum = 0
			for j in xrange(hs, he):
				for k in xrange(vs, ve):
					cur_sum += w[j][k] 
			if cur_sum == sum_req:
				continue
			else:
				#print hs, vs, he, ve, cur_sum
				print "Case #{}: IMPOSSIBLE".format(C)
				exit = 1
				break
			if exit == 1:
				break
		if exit == 1:
			break
	if exit == 1:
		continue
	print "Case #{}: POSSIBLE".format(C)
