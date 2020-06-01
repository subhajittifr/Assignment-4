#Problem 8:
import numpy as np 
import scipy

n=100000 #Number of points
def vol(dim):
	x=np.random.uniform(-1,1,(dim,n))
	k=0
	for i in range(n):
		s=0
		for j in range(dim):
			s+=x[j][i]**2 ## the norm of radius
		if s<1:
			k+=1
	I=k*(2**dim)/n #Volume estimation by Monte Carlo Intrgration 
	return I
print('Area of unit circle: ',vol(2))
print('Volume of 10 dimensional unit sphere: ',vol(10))



