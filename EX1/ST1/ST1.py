import numpy,scipy

def create_val():
	x = numpy.random.rand(8)*numpy.pi/8.0
	toReturn = numpy.sum(x)
	toReturn = numpy.sin(toReturn) * 10.0**6
	return toReturn

	
def evaluate_int(n):
	V = (numpy.pi/8.0)**8
	sumtot = 0
	sqsumtot = 0
	for i in range(0,n):
		x = create_val()
		sumtot +=x
		sqsumtot += x*x
	f = sumtot/n
	f2 = sqsumtot/n
	s = V*((f2-f**2)/n)**0.5
	diff = V*f-537.1873411
	return (diff,s)

intresults = []
stdresults = []
n =1000
for i in range(0,n):
	result = evaluate_int(1000)
	intresults.append(result[0])
	stdresults.append(result[1])

f = open('ST1_results.dat','w')
f.write('+/- Integral \t std \n')
for i in range(0,n):
	toWrite = str(intresults[i])+'\t'+str(stdresults[i])+'\n'
	f.write(toWrite)
f.close