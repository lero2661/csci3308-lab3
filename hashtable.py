def sumTwo(a, T):
	n = len(a)
	ht = [0] * 100
	foundpair = False
	
	for i in range(0, n-1):
		temp = T - a[i]
		if(temp >= 0 and ht[temp] == 1) :
			foundpair = True
			return True
		ht[a[i]] = 1
	if(not foundpair):
		return False


def sumThree(a, T):
	n = len(a)
	ht = [0] * 100
	foundtrio = False
	
	for i in range(0, n-1):
		if(sumTwo(a, T-a[i]) == True):
			foundtrio = True
			print 'trio found'
			return True
	
	if(not foundtrio):
		print 'no trio found'
		return False
		
a = [1, 3, 4, 5, 8]
b = [4, 5, 2, 18, 5, 9]
c = [1, 33, 4, 8, 15, 6]
print(sumTwo(a, 9))
print(sumTwo(b, 8))
print(sumThree(c, 13))

