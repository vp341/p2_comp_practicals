import numpy as np

def evaluate_int(n):
	V = (np.pi/8.0)**8
	x = np.random.rand(8,n)*np.pi/8.0
	x = np.sum(x,axis=0)
	x = np.sin(x)*10.0**6
	sumtot = np.sum(x)
	f = sumtot/n
	return V*f

n =50
means = []
stdevs = []


for this_length in range(1,10):
	intresults = []
	for i in range(0,n):
		result = evaluate_int(this_length*10**6)
		intresults.append(result)
	means.append(np.mean(intresults))
	stdevs.append(np.std(intresults))

f = open('CT1_results.dat','w')
f.write('n \t mean \t std \n')
for i in range(0,len(means)):
	toWrite = str((i+1)*10**7) +'\t' + str(means[i])+'\t'+str(stdevs[i])+'\n'
	f.write(toWrite)
f.close
#intvalue 537.187001574 +/- 0.0113829