#Problem 9:
import numpy as np 
import matplotlib.pyplot as plt 

def f(x):
	while(3<=x<=7):
		return 1/4
	else:
		return 0

nsteps=1000
theta0=3
steps,theta,theta_all=[],[],[]
for i in range(nsteps):
	theta1=np.random.rand()*7 #Generating ramdomnumber between 0 and 7
	r=np.random.rand()
	theta_all.append(theta1) # Storing all theta values 
	if (f(theta1)/f(theta0)>r):
		theta0=theta1
		theta.append(theta0)
		steps.append(i)
plt.figure
plt.suptitle("Markov chain and MCMC")
plt.subplot(211)
plt.hist(theta,bins=10,density='true',color="aquamarine",label='histogram')
plt.xlabel(r'$\theta$',fontsize=10)
plt.ylabel(r'$f(\theta)$',fontsize=16)
plt.legend()
plt.subplot(212)
plt.plot(steps,theta,label='Markov Chain',color='maroon')
plt.scatter(range(0,nsteps),theta_all,color='c')
plt.xlabel(r'$steps$',fontsize=16)
plt.ylabel(r'$\theta$',fontsize=16)
plt.legend()
plt.show()