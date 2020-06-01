import numpy as np 
import scipy
from scipy.stats import chi2
sample=11
obs_count1=[4,10,10,13,20,18,18,11,13,14,13]
obs_count2=[3,7,11,15,19,24,21,17,13,9,5]
n_times=[1,2,3,4,5,6,5,4,3,2,1]
p=[]
for i in range(sample):
	p.append(n_times[i]*1/36)
n=sum(obs_count1)
chisq_1,chisq_2=0,0
for i  in range(sample):
		chisq_1+=(obs_count1[i]-n*p[i])**2/(n*p[i])
		chisq_2+=(obs_count2[i]-n*p[i])**2/(n*p[i])

res_1=1-scipy.stats.chi2.cdf(chisq_1,10)
res_2=1-scipy.stats.chi2.cdf(chisq_2,10)
print('Probablity for chi2 less than',chisq_1,'for sample 1 is:',res_1)
print('Probablity for chi2 less than',chisq_2,'for sample 2 is:',res_2)
res=[res_1,res_2]
char=['First','Second']
for i in range(2):
	if(res[i]<=0.01 or res[i]>0.99):
		print( char[i],'Observation is Not Sufficiently Random')
	if(res[i]<=0.05 and res[i]>0.01 or res[i]<=0.99 and res[i]>0.95):
		print(char[i], 'Observation is Suspect')
	if(res[i]<=0.1 and res[i]>0.05 or res[i]<=0.95 and res[i]>0.90):
		print(char[i],'Observation is Almost Suspect')
	if(res[i]<=0.9 and res[i]>0.1):
		print(char[i],'Observation is Sufficiently Random')




    
