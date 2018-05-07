import sys

T = int(sys.stdin.readline().strip())

for C in xrange(1, T+1):
	N, P = map(int, sys.stdin.readline().strip().split())
	G = map(int, sys.stdin.readline().strip().split())
	out = 0
	rem = [0, 0, 0, 0]
	for i in G:
		rem[i % P] += 1
	if P == 2:
		out = rem[0] + (rem[1]/2) + (rem[1]%2)
	elif P == 3:
		out = rem[0] + min(rem[1], rem[2]) + (abs(rem[1] - rem[2])/3)
		if abs(rem[1] - rem[2]) % 3 != 0:
			out += 1
	else:
		out = rem[0] + min(rem[1], rem[3]) + (rem[2]/2)
		nrem1 = abs(rem[1] - rem[3]) 
		nrem2 = (rem[2] % 2)
		out += nrem1/4
		if nrem2:
			if (nrem1 % 4)  == 2:
				out += 1
			elif (nrem1 % 4)  == 3:
				out += 2
			elif (nrem1 % 4)  == 1:
				out += 1
			else:
				out += 1
		else:
			if nrem1 % 4:
				out += 1
	print "Case #{}: {}".format(C, out)
		

				
