import numpy
import scipy
from scipy import integrate


def fun_c(x):
	toReturn = numpy.cos(numpy.pi*x*x/2.0)
	return toReturn

def fun_s(x):
	toReturn = numpy.sin(numpy.pi*x*x/2.0)
	return toReturn

def int_c(lower,upper):
	toReturn = integrate.quad(fun_c,lower,upper)
	return toReturn[0]

def int_s(lower,upper):
	toReturn = integrate.quad(fun_s,lower,upper)
	return toReturn[0]

def calcplot(d):
	toLoop = numpy.arange(-5,5,0.01)
	delta = 10.0*numpy.sqrt(2.0/d)/2
	toReturn = []
	for i,val in enumerate(toLoop):
		x = int_c(val-delta,val+delta)
		y = int_s(val-delta,val+delta)
		amp = x*x + y*y
		phase = numpy.arctan(y/x)
		toReturn.append((amp,phase))
	return toReturn


d30 = calcplot(30)
d50 = calcplot(50)
d100 = calcplot(100)

f = open('ST2_results.dat','w')
f.write('d30amp \t d30phase \t d50amp \t d50phase \t d100amp \t d100phase \n')
for i in range(len(d30)):
	toWrite = str(d30[i][0]) + '\t' + str(d30[i][1]) + '\t' + str(d50[i][0]) + '\t' + str(d50[i][1]) + '\t' + str(d100[i][0]) + '\t' + str(d100[i][1])  + '\n'
	f.write(toWrite)
f.close