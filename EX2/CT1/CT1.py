import numpy as np
import scipy
from scipy import integrate
import matplotlib.pyplot as plt

def func(y, t , q, F):
	theta, omega = y
	dydt = [omega, -np.sin(theta)-q*omega + F*np.sin(2.0*t/3.0)]
	return dydt


def energy(y):
	theta,omega = y
	e = (omega**2) /2.0+ (1-np.cos(theta))
	return e

def signchange(x,y):
	toReturn = 0
	if (np.sign(x[0])-np.sign(y[0]) != 0):
		toReturn = 1
	return toReturn

def period(sol):
	changes = 1
	for i in range(1,len(sol)):
		if (signchange(sol[i-1],sol[i])):
			changes += 1
	return changes

def indivperiod(theta0):
	y0 = [theta0,0.0]
	sol = integrate.odeint(func,y0,t,args=(q,F))
	this_period = period(sol)
	period_i = 2*totalTime/this_period
	return period_i

q = 0
F = 0
totalTime = 1000
noOfSteps = 10000
t = np.linspace(0,totalTime,noOfSteps)
thetas = np.linspace(0.01*np.pi,0.99*np.pi,199)
print(thetas[99]/np.pi)
thetavperiod = []

for theta in thetas:
	this_per = indivperiod(theta)
	thetavperiod.append((theta,this_per))

t2 = np.linspace(0,10000,10000)
sol = integrate.odeint(func,[0.01,0],t2,args=(q,F))
energies = []
for step in sol:
	energies.append(energy(step))

f = open('CT1_results_1.dat','w')
f.write('Time \t Energy \n')
for i in range(0,len(energies)):
	toWrite = str(t2[i])+'\t'+str(energies[i]-energies[0])+'\n'
	f.write(toWrite)
f.close

f = open('CT1_results_2.dat','w')
f.write('Inital Angle \t Period \n')
for i in range(0,len(thetavperiod)):
	toWrite = str(thetavperiod[i][0])+'\t'+str(thetavperiod[i][1])+'\n'
	f.write(toWrite)
f.close

# print(sol[100],energy(sol[100]))
# print(sol[1000], energy(sol[1000]))
# print (sol[10000], energy(sol[10000]))
# print (sol[100000], energy(sol[100000]))

# plt.plot(t, sol[:, 0], 'b', label='theta(t)')
# plt.plot(t, sol[:, 1], 'g', label='omega(t)')
# plt.legend(loc='best')
# plt.xlabel('t')
# plt.grid()
# plt.show()
