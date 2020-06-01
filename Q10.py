#Problem 10:

import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt('Q10.txt',delimiter='&')
x=data[:,1]
y=data[:,2]
sigma_y=data[:,3]


def log_likelihood(theta, x, y, yerr):
	a,b,c = theta
	model = a*x*x+b*x+c
	sigma_y2 = yerr**2
#negative lnL
	return (0.5*np.sum((y - model)**2/sigma_y2 +np.log(2*np.pi*sigma_y2)))

def log_prior(theta):
	a,b,c = theta
	if (-500.0< a <500.0 and -500.0< b <1000.0 and -500.< c <500.0):
		return (0.0)
	return (-np.inf)

def log_probability(theta, x, y, yerr):
	lp = log_prior(theta)
	if not np.isfinite(lp):
		return (-np.inf)
	return (lp - log_likelihood(theta, x, y, yerr))

from scipy.optimize import minimize
guess = (1.0, 8.0, 10.0)
soln = minimize(log_likelihood,guess,args=(x, y, sigma_y))
nwalkers, dim =50,3
pos = soln.x + 1e-4*np.random.randn(nwalkers, dim)
#####################################
import emcee
sampler=emcee.EnsembleSampler(nwalkers,dim,log_probability,args=(x, y, sigma_y))
sampler.run_mcmc(pos, 4000)
samples = sampler.get_chain() 
samples_data = sampler.get_chain(discard=200,thin=30,flat=True)
fig1=plt.figure
plt.subplot(311)
plt.plot(samples[:,:,0],'-k',linewidth='0.5')
plt.ylabel(r'$a$',fontsize=16)
plt.subplot(312)
plt.plot(samples[:,:,1],'-k',linewidth='0.5')
plt.ylabel(r'$b$',fontsize=16)
plt.subplot(313)
plt.plot(samples[:,:,2],'-k',linewidth='0.5')
plt.ylabel(r'$c$',fontsize=16)

###########################################
import corner 

medians = np.median(samples_data,axis=0)
a_true,b_true,c_true= medians
labels=["a","b","c"]
fig2=corner.corner(samples_data,labels=labels,truths=[a_true,b_true,c_true])
###########################
fig3=plt.figure()

x0=np.linspace(40,300,1000)
y_best=a_true*x0**2+b_true*x0+c_true					#Best fit for the given model
points=np.random.randint(len(samples_data), size=200)
for i in points:
	s=samples_data[i]
	a,b,c=s[:3]
	y_rand=a*x0**2+b*x0+c						#plotting random 200 models choosen from the posterior
	plt.plot(x0,y_rand,'maroon')						
plt.errorbar(x,y,yerr=sigma_y,fmt=".k",capsize=3,label="errorbars")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x0,y_best,"c",label="best fit")
plt.legend()
plt.show()
