import numpy as np
def create_val(n):
	x = np.random.rand(8)*np.pi/8.0
	toReturn = np.sum(x)
	toReturn = np.sin(toReturn) * 10.0**6
	return toReturn

	
def evaluate_int(n):
	V = (np.pi/8.0)**8
	sumtot = 0
	sqsumtot = 0
	int_set = np.fromfunction(create_val,(n,))
	sumtot = np.sum(int_set)
	f = sumtot/n
	return V*f

n =50
exp = 9
means = []
stdevs = []


for this_exp in range(0,exp):
	intresults = []
	for i in range(0,n):
		result = evaluate_int(10**this_exp)
		intresults.append(result)
		print(i)
	means.append(np.mean(intresults))
	stdevs.append(np.std(intresults))




f = open('CT1_results.dat','w')
f.write('n \t mean \t std \n')
for i in range(0,exp):
	toWrite = str(10**i) + str(means[i])+'\t'+str(stdevs[i])+'\n'
	f.write(toWrite)
f.close


#print("mean "+str(mean)+" stdev "+str(stdev))
