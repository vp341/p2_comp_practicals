import numpy
import scipy
from scipy import integrate


def fun_c(x):
	toReturn = numpy.cos(numpy.pi*x*x/2.0)
	return toReturn

def fun_s(x):
	toReturn = numpy.sin(numpy.pi*x*x/2.0)
	return toReturn

def int_c(u):
	toReturn = integrate.quad(fun_c,0,u)
	return toReturn[0]

def int_s(u):
	toReturn = integrate.quad(fun_s,0,u)
	return toReturn[0]

toLoop = numpy.arange(-8,8,0.01)


f = open('CT2_results.dat','w')
f.write('x \t y \n')
for i in toLoop:
	x = int_c(i)
	y = int_s(i)
	toWrite = str(x) + '\t' + str(y) + '\n'
	f.write(toWrite)
f.close

