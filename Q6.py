import numpy as np
import matplotlib.pyplot as plt
n=10000

def f(x):
    return np.sqrt(2/np.pi)*np.exp((-x**2)/2)
def g(x):
	return 1.5*np.exp(-x)

x=np.random.rand(n)
x=-np.log(x)
y=np.random.rand(n)*g(x)
x_good=x[y<f(x)]
x1=np.linspace(0,6,n)
plt.hist(x_good,range=(0,6),bins=50,density='true',color="c")
plt.plot(x1,f(x1),color='maroon',label=r'$f(x)$')
plt.plot(x1,g(x1),color='orangered',label=r'$g(x)=1.5 e^{-x}$')
plt.xlabel(r'$x$',fontsize=16)
plt.ylabel(r'$f(x)$',fontsize=16)
plt.text(3,0.6, r"$Rejection \ Method$", fontsize=14)
plt.legend()
plt.show()
