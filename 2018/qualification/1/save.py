import sys

T=int(sys.stdin.readline())

def calc_damage(code):
	beam = 1
	damage = 0
	for i in code:
		if i == 'C':
			beam = beam * 2
		else:
			damage += beam
	return [damage, beam]

def gentab(code, beam):
	count = 0
	out = []
	for i in code[::-1]:
		if i == 'S':
			count += 1
		else:
			out.append(count)
	return out
			
		
for i in xrange(T):
	istr = sys.stdin.readline().split()
	d = int(istr[0])
	code = istr[1]
	l = len(code)
	min_damage = code.count('S')
	if min_damage > d:
		print "Case #" + str(i+1) + ": IMPOSSIBLE"
		continue
	damage, beam = calc_damage(code)
	swaps = 0
	if damage < d:
		print "Case #" + str(i+1) + ": 0"
		continue	
	sarr = gentab(code, beam)
#	print damage, beam, sarr
	dif = damage - d
	count = 0
	for j in sarr:
		if j == 0:
			beam = beam / 2
			continue
		reduction = beam / 2 * j
		if dif > reduction:
			count += j
			beam = beam / 2
			dif = dif - reduction
		else:
			x = (dif/(beam/2))
			if x*(beam/2) == dif:
				count += x
			else:
				count += x + 1
			break
	print "Case #" + str(i+1) + ": " + str(count) 
	
