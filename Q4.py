import numpy as np
import matplotlib.pyplot as plt
n=1000

def f(x):
	return 2*np.exp(-2*x)

file=open('Q4.txt','r')
y=[]

for line in file:
    y1=line
    y.append(float(y1))


x1=np.linspace(0,4,n)
plt.hist(y,range=(0,4),bins=50,density='true',color="c",label='Histogram')
plt.plot(x1,f(x1),color='maroon',label=r'$p(x)$')
# plt.plot(x1,g(x1),color='orangered',label=r'$f(x)=\frac{1}{2} e^{-\frac{1}{2} x}$')
plt.xlabel(r'$x$',fontsize=16)
plt.ylabel(r'$PDF$',fontsize=16)
plt.text(2.5,1, r"$p(x)=2 e^{-2 x}$", fontsize=14)
plt.legend()
plt.show()