import sys

T = int(sys.stdin.readline().strip())

for C in xrange(1, T+1):
	r, c = map(int, sys.stdin.readline().strip().split())
	grid = []
	for i in xrange(r):
		row = sys.stdin.readline().strip()
		grid.append(row)
	count = 0
	exit = 0
	singles = {}
	for i in xrange(r):
		rc = 0
		first = '.'
		last = '.'
		fi = 0
		fj = 0
		for j in xrange(c):
			if grid[i][j] == '.':
				continue
			rc += 1
			if rc == 1:
				first = grid[i][j]
				fi = i
				fj = j
			last = grid[i][j] 
		if rc == 1:
			singles[(fi, fj)] = 1

		if first == '<':
			count += 1
		if last == '>':
			count += 1

	for i in xrange(c):
		cc = 0
		first = '.'
		last = '.'
		fi = 0
		fj = 0
		for j in xrange(r):
			if grid[j][i] == '.':
				continue
			cc += 1
			if cc == 1:
				first = grid[j][i]
				fi = i
				fj = j
			last = grid[j][i]
		if cc == 1:
			if singles.has_key((fj, fi)):
				print "Case #{}: IMPOSSIBLE".format(C)
				exit = 1
				break
		if exit == 1:		
			break

		if first == '^':
			count += 1
		if last == 'v':
			count += 1
		
	if exit == 1:
		continue	
	print "Case #{}: {}".format(C, count)	
