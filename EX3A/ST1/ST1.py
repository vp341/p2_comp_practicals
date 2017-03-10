import numpy as np
import matplotlib.pyplot as plt

def phase(x,s,m):
	toReturn = np.exp(1j*(m/2)*np.sin(2*np.pi*x/s))
	return toReturn

def phase_factor(x,l,D):
	k = 2*np.pi/l
	toReturn = np.exp(1j*k*x**2/(2*D))
	return toReturn

def central_slit(array_sizes,d,L,l,D):
	toReturn = np.zeros(array_sizes)
	width = d/L * array_sizes
	center = array_sizes/2
	w_plus = round(center + width/2)
	w_minus = round(center - width/2)
	print(center,w_plus,w_minus)
	phase_factored = np.linspace(-d/2,d/2,w_plus-w_minus,dtype=complex)
	phase_factored = phase_factor(phase_factored,l,D)
	toReturn[w_minus:w_plus]= phase_factored
	return toReturn

def central_slit_phase(array_sizes,d,L,s,m,l,D):
	toReturn = np.zeros(array_sizes,dtype = complex)
	width = d/L * array_sizes
	center = array_sizes/2
	w_plus = round(center + width/2)
	w_minus = round(center - width/2)
	toAssign = np.linspace(-d/2,d/2,w_plus-w_minus,dtype=complex)
	toAssign = phase(toAssign,s,m)
	phase_factored = np.linspace(-d/2,d/2,w_plus-w_minus,dtype=complex)
	phase_factored = phase_factor(phase_factored,l,D)
	toAssign = phase_factored*toAssign
	toReturn[w_minus:w_plus]= toAssign
	return toReturn

l = 500e-9 #wavelength
L = 5e-3 #aperture length

d1 = 100e-6 # slit width
d2 = 2e-3
D2 = 0.5 #screen - source distance
s = 100e-6 #phase spacing of aperture
m = 8

D1 = 5e-3

array_sizes = 2**18
x1 = np.fft.fftshift(np.fft.fftfreq(array_sizes,L/array_sizes))
x1 = x1*l*D1/(2*np.pi)
A1 = central_slit(array_sizes,d1,L,l,D1)
fft1 = np.fft.fftshift(np.fft.fft(A1))
fft1 = fft1/np.max(fft1)
fft12 = np.abs(fft1)**2
#plt.plot(x,analytic,'r',label='Analytic')
plt.plot(x1,np.real(fft1), 'b', label='FFT')
plt.plot(x1,np.imag(fft1), 'g', label='IMAG FFT')
plt.plot(x1,fft12,'r',label = 'FFT Intensity')
plt.xlabel('y / m')
plt.ylabel('Relative Intensity')
plt.legend(loc='best')
plt.grid()
plt.show()

x2 = np.fft.fftshift(np.fft.fftfreq(array_sizes,L/array_sizes))
x2 = x2*l*D2/(2*np.pi)
A2 = central_slit_phase(array_sizes,d2,L,s,m,l,D2)
fft2 = np.fft.fftshift(np.fft.fft(A2))
fft2 = fft2/np.max(fft2)
fft22 = np.abs(fft2)**2
#plt.plot(x,analytic,'r',label='Analytic')
plt.plot(x2,np.real(fft2), 'b', label='FFT')
plt.plot(x2,np.imag(fft2), 'g', label='IMAG FFT')
plt.plot(x2,fft22,'r',label = 'FFT Intensity')
plt.xlabel('y / m')
plt.ylabel('Relative Intensity')
plt.legend(loc='best')
plt.grid()
plt.show()
