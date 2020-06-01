import numpy as np 
import matplotlib.pyplot as plt
import time 
t1=time.time()
a=12453756.56
c=120.345
m=1
n=10000 
x=1.0

results=[]
for i in range(n):
	x=(a*x+c)%m
	results.append(x)
bins=30
x1=np.linspace(0,1,bins)
plt.hist(results,range=(0,1),bins=bins,density='true',color="c")
plt.plot(x1,np.ones(bins),color='orangered',label='PDF')
plt.xlabel(r'$x$',fontsize=16)
plt.ylabel(r'$f(x)$',fontsize=16)
plt.text(0.5,0.5, r"$Without \ Using \ Numpy$",color='azure',fontsize=14)
plt.legend()
t2=time.time()
print('Time taken for problem 1:',t2-t1,'s')
plt.show()
