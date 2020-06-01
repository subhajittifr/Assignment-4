import numpy as np
import matplotlib.pyplot as plt
def f(x):
	return (1/np.sqrt(2*np.pi))*np.exp((-x**2)/2)

n=10000
x1=np.random.rand(n)
x2=np.random.rand(n)
x=np.linspace(-10,10,100)
y1=np.sqrt(-2*np.log(x1))*np.cos(2*np.pi*x2)
y2=np.sqrt(-2*np.log(x1))*np.sin(2*np.pi*x2)
fig=plt.figure()
plt.subplot(2,2,1)
plt.hist(x1,range=(0,1),bins=10,density='true',color="c",label='histogram')
plt.xlabel(r'$x_1$',fontsize=10)
plt.ylabel(r'$PDF$',fontsize=10)
plt.subplot(2,2,2)
plt.hist(x1,range=(0,1),bins=10,density='true',color="salmon",label='histogram')
plt.xlabel(r'$x_2$',fontsize=10)
plt.ylabel(r'$PDF$',fontsize=10)
plt.subplot(2,2,3)
plt.plot(x,f(x),'k')
plt.hist(y1,range=(-10,10),bins=50,density='true',color="c",label='histogram')
plt.xlabel(r'$y_1$',fontsize=10)
plt.ylabel(r'$PDF$',fontsize=10)

plt.subplot(2,2,4)
plt.plot(x,f(x),'k')
plt.hist(y2,range=(-10,10),bins=50,density='true',color="salmon",label='histogram')
plt.xlabel(r'$y_2$',fontsize=10)
plt.ylabel(r'$PDF$',fontsize=10)

plt.show()
