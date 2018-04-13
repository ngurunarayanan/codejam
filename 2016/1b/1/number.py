import sys

T = int(sys.stdin.readline().strip())

for C in xrange(1, T+1):
	d = {}
	s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in s:
		d[i] = 0
	s = sys.stdin.readline().strip()
	for i in s:
		d[i] += 1
	out = []
	#0
	n = d['Z']
	if n:
		d['Z'] -= n
		d['E'] -= n
		d['R'] -= n
		d['O'] -= n
	for i in xrange(n):
		out.append(0)
	#2
	n = d['W']
	if n:
		d['T'] -= n
		d['W'] -= n
		d['O'] -= n
	for i in xrange(n):
		out.append(2)

	#4
	n = d['U']
	if n:
		d['F'] -= n
		d['O'] -= n
		d['U'] -= n
		d['R'] -= n
	for i in xrange(n):
		out.append(4)

	#5
	n = d['F']
	if n:
		d['F'] -= n
		d['I'] -= n
		d['V'] -= n
		d['E'] -= n
	for i in xrange(n):
		out.append(5)

	#6
	n = d['X']
	if n:
		d['S'] -= n
		d['I'] -= n
		d['X'] -= n
	for i in xrange(n):
		out.append(6)


	#7
	n = d['S']
	if n:
		d['S'] -= n
		d['E'] -= n
		d['V'] -= n
		d['E'] -= n
		d['N'] -= n
	for i in xrange(n):
		out.append(7)


	#8
	n = d['G']
	if n:
		d['E'] -= n
		d['I'] -= n
		d['G'] -= n
		d['H'] -= n
		d['T'] -= n
	for i in xrange(n):
		out.append(8)

	#3
	n = d['H']
	if n:
		d['T'] -= n
		d['H'] -= n
		d['R'] -= n
		d['E'] -= n
		d['E'] -= n
	for i in xrange(n):
		out.append(3)

	#1
	n = d['O']
	if n:
		d['O'] -= n
		d['N'] -= n
		d['E'] -= n
	for i in xrange(n):
		out.append(1)

	n = d['I']
	if n:
		d['N'] -= n
		d['I'] -= n
		d['N'] -= n
		d['E'] -= n
	for i in xrange(n):
		out.append(9)

	out.sort()
	out = map(str, out)
	out_str = reduce(lambda x, y: x + y, out)
	print "Case #{}: {}".format(C, out_str)
