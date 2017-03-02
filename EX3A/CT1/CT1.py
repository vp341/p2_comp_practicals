import numpy as np
import matplotlib.pyplot as plt

def central_slit(array_sizes,d,L):
	toReturn = np.zeros(array_sizes)
	width = d/L * array_sizes
	center = array_sizes/2
	w_plus = round(center + width/2)
	w_minus = round(center - width/2)
	print(center,w_plus,w_minus)
	toReturn[w_minus:w_plus]= 1.0
	return toReturn

l = 500e-9 #wavelength
L = 5e-3 #aperture length
d = 100e-6 # slit width
D = 1 #screen - source distance
array_sizes = 2**10
delta = array_sizes/D
x = np.fft.fftshift(np.fft.fftfreq(array_sizes,L/array_sizes))
x = x*l*D/(2*np.pi)
A = central_slit(array_sizes,d,L)
fft = np.fft.fftshift(np.fft.fft(A))
fft = fft/np.max(fft)
fft2 = np.abs(fft)**2
reduced_x = 2*x*np.pi*d/(l*D)
analytic = np.sinc(reduced_x)**2
plt.plot(x,analytic,'r',label='Analytic')
plt.plot(x,abs(fft2), 'b', label='FFT')
plt.xlabel('y / m')
plt.ylabel('Relative Intensity')
plt.xlim([-0.0020,0.0020])
plt.legend(loc='best')
plt.grid()
plt.show()
