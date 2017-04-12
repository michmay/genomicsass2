#!usr/bin/python
import numpy as np


s=list(range(17))
for i in range(17):
	s[i]='S'+str(i+1)
s.append('SN')

npar = np.identity(17)
npar = np.c_[np.zeros(17),npar]
npar = np.r_[npar,[np.zeros(len(npar[0]))]]
npar[-1][-1] = 199/200
npar[-1][0] = 1/200

with open('transitions.txt','w') as f:
    for i in s:
        f.write('\t'+i)
    f.write('\n')
    for i in range(len(npar)):
        f.write(s[i]+'\t')
        for j in npar[i]:
            f.write(str(j)+'\t')
        f.write('\n')


#fix l




