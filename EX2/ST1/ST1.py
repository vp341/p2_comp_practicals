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

def signchange_omega(x,y):
	toReturn = 0
	if (np.sign(x[1])-np.sign(y[1]) != 0):
		toReturn = 1
	return toReturn

def period(sol):
	changes = 1
	for i in range(1,len(sol)):
		if (signchange_omega(sol[i-1],sol[i])):
			changes += 1
	return changes

def indivperiod(theta0):
	y0 = [theta0,0.0]
	sol = integrate.odeint(func,y0,t,args=(q,F))
	this_period = period(sol)
	period_i = 2*totalTime/this_period
	return period_i

q = 0.5
F = 1.2
totalTime = 150
noOfSteps = 10000

t = np.linspace(0,totalTime,noOfSteps)

sol1 = integrate.odeint(func,[0.2,0],t,args=(q,F))
sol2 = integrate.odeint(func,[0.20001,0],t,args=(q,F))

dif = sol2-sol1

plt.plot(t, dif[:,0], 'b', label='theta')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()

