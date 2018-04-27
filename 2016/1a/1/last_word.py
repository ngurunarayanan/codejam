import sys

T = int(sys.stdin.readline().strip())
for C in xrange(1, T+1):
	s = sys.stdin.readline().strip()

	out = s[0:1]
	for i in s[1:]:
		if i >= out[0]:
			out = str(i) + out
		else:
			out = out + str(i)

	print "Case #{}: {}".format(C, out)
		
	
	
