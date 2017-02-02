<<<<<<< HEAD
hello world






bye
=======

celebtimes = [(2, 53), (5, 50), (5, 98), (102, 150), (120, 186), (85, 190)]
celebtimes2 = [(5, 20), (15, 40), (35, 50), (37, 47), (45, 55)]

def adtime(celebtimes):
	sortedtimes = sorted(celebtimes)
	n = len(sortedtimes)
	leastuj = sortedtimes[0][1]
	adtimes = []
	print(sortedtimes)
	for i in range(n):
		if sortedtimes[i][1] <= leastuj and sortedtimes[i][1] < sortedtimes[i+1][1]:
			leastuj = sortedtimes[i][1]
			adtimes.append(leastuj)
		if(sortedtimes[i][0] > leastuj):
			leastuj = sortedtimes[i][1]
			if sortedtimes[i][1] < leastuj:
				leastuj = sortedtimes[i][1]
				adtimes.append(leastuj)
	print(adtimes)
		


adtime(celebtimes)
adtime(celebtimes2)
>>>>>>> testing-new-files
