import sys

T = int(sys.stdin.readline().strip())

for C in xrange(1, T+1):
#	sys.stderr.write("\n==\n")
	n = int(sys.stdin.readline().strip())
	avail = [1 for i in xrange(n)]
	probs = [.005 for i in xrange(n)]
	counts = [0 for i in xrange(n)]
	for i in xrange(n):
		likes = map(int, sys.stdin.readline().strip().split())
		d = likes[0]
		likes = likes[1:]
		if d == 0:
			print "-1"
			sys.stdout.flush()
			continue
		for j in likes:
			counts[j] += 1
		cur_avail = []
		for j in likes:
			if avail[j] == 1:
				cur_avail.append([j, counts[j]])
#				avail[j] = 0
#				print "{}".format(j)
#				break
		if len(cur_avail) == 0:
			sys.stderr.write("\nCur_avail = 0\n")		
			print "-1"
			sys.stdout.flush()
			continue
#		sys.stderr.write("\n" + str(cur_avail) + "\n")
#		sys.stderr.flush()
		cur_na = sorted(cur_avail, key=lambda x: x[1])
		print cur_na[0][0]
		sys.stdout.flush()
		avail[cur_na[0][0]] = 0


