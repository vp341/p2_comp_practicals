import numpy as np
import matplotlib.pyplot as plt

def phase(x,s,m):
	toReturn = np.exp(1j*(m/2)*np.sin(2*np.pi*x/s))
	return toReturn

def central_slit(array_sizes,d,L,s,m):
	toReturn = np.zeros(array_sizes,dtype = complex)
	width = d/L * array_sizes
	center = array_sizes/2
	w_plus = round(center + width/2)
	w_minus = round(center - width/2)
	toAssign = np.linspace(-d/2,d/2,w_plus-w_minus,dtype=complex)
	toAssign = phase(toAssign,s,m)
	toReturn[w_minus:w_plus]= toAssign
	return toReturn

l = 500e-9 #wavelength
L = 5e-3 #aperture length
d = 2e-3 # slit width
D = 10 #screen - source distance
s = 100e-6 #phase spacing of aperture
m = 8
array_sizes = 2**18
delta = array_sizes/D
x = np.fft.fftshift(np.fft.fftfreq(array_sizes,L/array_sizes))
x = x*l*D/(2*np.pi)
A = central_slit(array_sizes,d,L,s,m)
fft = np.fft.fftshift(np.fft.fft(A))
fft = fft/np.max(fft)
fft2 = np.abs(fft)**2
reduced_x = 2*x*np.pi*d/(l*D)
analytic = np.sinc(reduced_x)**2
#plt.plot(x,analytic,'r',label='Analytic')
#plt.plot(x,np.real(fft), 'b', label='FFT')
#plt.plot(x,np.imag(fft), 'g', label='IMAG FFT')
#plt.plot(x,fft2,'r',label = 'FFT Intensity')
plt.plot(x,fft2,'r',label = '')
plt.xlabel('y / m')
plt.ylabel('Relative Intensity')
plt.legend(loc='best')
plt.grid()
plt.show()
