import sys

T = int(sys.stdin.readline())

for i in xrange(T):
	n = int(sys.stdin.readline())
	arr = map(long, sys.stdin.readline().split())
	done = False
	while not done:
		done = True
		for j in xrange(n-2):
			if arr[j] > arr[j+2]:
				done = False
				tmp = arr[j]
				arr[j] = arr[j + 2]
				arr[j + 2] = tmp
	
#	print arr		
	for j in xrange(n-1):
		if arr[j] > arr[j+1]:
			print "Case #" + str(i+1) + ": " + str(j)
			sys.stdout.flush()
			break
	else:
		print "Case #" + str(i+1) + ": OK"
		sys.stdout.flush()
