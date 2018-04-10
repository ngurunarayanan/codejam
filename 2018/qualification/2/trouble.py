import sys

T = int(sys.stdin.readline())

for i in xrange(T):
	n = int(sys.stdin.readline())
	arr = map(long, sys.stdin.readline().split())
	even = arr[0:][::2]
	odd = arr[1:][::2]
	even.sort()
	odd.sort()
	ne = n / 2
	no = n / 2
	if n % 2 != 0:
		ne += 1
	index = 0
	for j in xrange(ne-1):
		if even[j] > odd[j]:
			print "Case #" + str(i+1) + ": " + str(index)
			sys.stdout.flush()
			break
		index += 1
		if odd[j] > even[j + 1]:
			print "Case #" + str(i+1) + ": " + str(index)
			sys.stdout.flush()
			break
		index += 1
	else:
		if ne == no:
			if even[ne-1] > odd[no-1]:
				print "Case #" + str(i+1) + ": " + str(index)
				sys.stdout.flush()
				continue
		print "Case #" + str(i+1) + ": OK"
		sys.stdout.flush()

