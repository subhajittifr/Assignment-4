import numpy as np 
import matplotlib.pyplot as plt
import time 
t1=time.time()
n=10000
results=np.random.rand(10000)

bins=30
x1=np.linspace(0,1,bins)
plt.hist(results,range=(0,1),bins=bins,density='true',color="teal")
plt.plot(x1,np.ones(bins),color='indigo',label='PDF')
plt.xlabel(r'$x$',fontsize=16)
plt.ylabel(r'$f(x)$',fontsize=16)
plt.text(0.5,0.5, r"$Using \ Numpy$",color='red',fontsize=14)
plt.legend()

t2=time.time()

print('Time taken for problem 2:',t2-t1,'s')

plt.show()