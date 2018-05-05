import sys

T = int(sys.stdin.readline().strip())

for C in xrange(1, T+1):
	n, l = map(int, sys.stdin.readline().strip().split())
	counts = [0 for i in xrange(l)]
	dics = [{} for i in xrange(l)]
	word_dics = {}
	words = []
	for i in xrange(n):
		s = sys.stdin.readline().strip()
		for j in xrange(l):
			if dics[j].has_key(s[j]):
				dics[j][s[j]] += 1
				continue
			else:
				dics[j][s[j]] = 1
				counts[j] += 1
		words.append(s)
		word_dics[s] = 1
	total = 1
#	print counts
	for i in xrange(l):
		total = total * counts[i] 
#	print total
	if total == n:
		print "Case #{}: -".format(C)
		continue
	exit = 0
	for i in xrange(l):
		for j in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			if dics[i].has_key(j) and dics[i][j] < n and dics[i][j] < total/counts[i]:
				for k in words:
					nw = k[:i] + str(j) + k[i+1:]
					if word_dics.has_key(nw):
						continue
					else:
						print "Case #{}: {}".format(C, nw)
						exit = 1
						break
			if exit == 1:
				break
		if exit == 1:
			break				
#	else:
#		nw = words[0][:l-1]
#		for i in xrange(1, n):
#			if words[i][l-1] != words[0][l-1]:
#				nw += words[i][l-1:]
#				break
#		print "Case #{}: {}".format(C, nw) 
		
		
