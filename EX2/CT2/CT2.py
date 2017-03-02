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
qs = [1,5,10]
F = 0
totalTime = 1000
noOfSteps = 10000
Fs = [0.5,1.2,1.44,1.465]

t = np.linspace(0,totalTime,noOfSteps)

q_sols = []
f_sols = []
f_periods = []

for q_i in qs:
	q_sols.append(integrate.odeint(func,[1,0.0],t,args=(q_i,F)))

for F_i in Fs:
	f_sol = integrate.odeint(func,[0.01,0.0],t,args=(q,F_i))
	f_period = 2*totalTime / period(f_sol)
	print(f_period)
	f_sols.append(f_sol)
	f_periods.append(f_period)

# print(sol[100],energy(sol[100]))
# print(sol[1000], energy(sol[1000]))
# print (sol[10000], energy(sol[10000]))
# print (sol[100000], energy(sol[100000]))

# for plotting q_sols
plt.plot(t, q_sols[0][:, 0], 'b', label='theta, q = 1')
#plt.plot(t, q_sols[0][:, 1], 'g', label='omega, q = 1')
plt.plot(t, q_sols[1][:, 0], 'r', label='theta, q = 5')
#plt.plot(t, q_sols[1][:, 1], 'k', label='omega, q = 5')
plt.plot(t, q_sols[2][:, 0], 'c', label='theta, q = 10')
#plt.plot(t, q_sols[2][:, 1], 'm', label='omega, q = 10')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()

plt.plot(Fs, f_periods,'b', label='')
plt.legend(loc='best')
plt.xlabel('F')
plt.ylabel('Period /s')
plt.grid()
plt.show()