import sys

T = int(sys.stdin.readline().strip())

def sort_out(out_str):
	n = len(out_str)
	if n == 2:
		return out_str	
	s1 = sort_out(out_str[:n/2])
	s2 = sort_out(out_str[n/2:]) 
	if s1 < s2:
		return s1 + s2
	else:
		return s2 + s1

for C in xrange(1, T+1):
	n, r, p, s = map(int, sys.stdin.readline().strip().split())
	a = [r, p, s]
	a.sort()
	if a[0] == a[1]:
		if a[2] == a[0] + 1:
			pass
		else:
			print "Case #{}: IMPOSSIBLE".format(C)
			continue
	else:
		if a[1] == a[2] and a[0] == a[1] - 1:
			pass
		else:
			print "Case #{}: IMPOSSIBLE".format(C)
			continue
	out1 = []
	out1.append(['P'])
	ro = 0
	po = 0
	so = 0
	for i in xrange(1, n+1):
		s1 = ""
		for j in out1[i-1]:
			if j == 'P':
				s1 += "PR"
			elif j == 'R':
				s1 += "RS"
			else:
				s1 += "PS"
		out1.append(s1)
	for i in out1[n]:
		if i == 'R':
			ro += 1
		elif i == 'P':
			po += 1
		else:
			so += 1
	if ro == r and po == p and so == s:
		out = out1[n]
		out = sort_out(out)
		print "Case #{}: {}".format(C, out)
		continue 

#	print "{}:{}:{}".format(r, p, s)
#	print "{}".format(out1[n])
#	print "{}:{}:{}==".format(ro, po, so)
	
	ro = 0
	po = 0
	so = 0
	out2 = []
	out2.append(['R'])

	for i in xrange(1, n+1):
		s1 = ""
		for j in out2[i-1]:
			if j == 'P':
				s1 += "PR"
			elif j == 'R':
				s1 += "RS"
			else:
				s1 += "PS"
		out2.append(s1)
	for i in out2[n]:
		if i == 'R':
			ro += 1
		elif i == 'P':
			po += 1
		else:
			so += 1
	if ro == r and po == p and so == s:
		out = out2[n]
		out = sort_out(out)
		print "Case #{}: {}".format(C, out)
		continue 
#	print "{}:{}:{}".format(r, p, s)
#	print "{}".format(out2[n])
#	print "{}.{}.{}".format(ro, po, so)

	ro = 0
	po = 0
	so = 0
	out3 = []
	out3.append(['S'])

	for i in xrange(1, n+1):
		s1 = ""
		for j in out3[i-1]:
			if j == 'P':
				s1 += "PR"
			elif j == 'R':
				s1 += "RS"
			else:
				s1 += "PS"
		out3.append(s1)
	for i in out3[n]:
		if i == 'R':
			ro += 1
		elif i == 'P':
			po += 1
		else:
			so += 1
	if ro == r and po == p and so == s:
		out = out3[n]
		out = sort_out(out)
		print "Case #{}: {}".format(C, out)
		continue 

#	print "{}:{}:{}".format(r, p, s)
#	print "{}".format(out3[n])
#	print "{}.{}.{}".format(ro, po, so)
			 
		
