import sys

T = int(sys.stdin.readline().strip())

for C in xrange(1, T+1):
	ac, aj = map(int, sys.stdin.readline().strip().split())
	cs = []
	ce = []
	js = []
	je = []
	jobs = []
	jobe = []
	for i in xrange(ac):
		s, e = map(int, sys.stdin.readline().strip().split())
		cs.append(s)
		ce.append(e)
		jobs.append(s)
		jobe.append(e)
	for i in xrange(aj):
		s, e = map(int, sys.stdin.readline().strip().split())
		cs.append(s)
		ce.append(e)
		jobs.append(s)
		jobe.append(e)
	jobs.sort()
	jobe.sort()
	if ac == 1 and aj == 1:
		print "Case #{}: 2".format(C)
		continue
	elif len(jobs) < 2:
		print "Case #{}: 2".format(C)
		continue
	else:
		if jobe[1] - jobs[0] <= 720:
			print "Case #{}: 2".format(C)
			continue
		elif jobe[0] + 1440 - jobs[1] <= 720:
			print "Case #{}: 2".format(C)
			continue
		else:
			print "Case #{}: 4".format(C)
