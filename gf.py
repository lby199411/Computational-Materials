#!/hpcgpfs01/ic2software/anaconda/2023.07/bin/python
import numpy as np
from tabulate import tabulate
def WriteForce(outdata):
    '''
    Calculate the max force in the system for each ionic steps
    '''
    flag = False
    f, maxf, e = [], [], []
    i = 0
    fmax = 0
    while i < len(outdata):
        if not flag:
            if "TOTAL-FORCE" in outdata[i]:
                flag = True
                i += 2
                continue
            else:
                if 'energy  without' in outdata[i]:
                    e.append(outdata[i].split()[3])
                i += 1
        if flag:
            if outdata[i][1] == '-':
               # print(f)
                for j in f:
                    fval = (float(j[0])**2 + float(j[1])**2 + float(j[2])**2)**(1./2.)
                    if fval > fmax:
                        fmax = fval
                maxf.append(str(fmax))
                f = []
                flag = False
                i += 1
                fmax = 0
            else:
                f.append(outdata[i].split()[3:6])
                i += 1
    return maxf, e
'''    try:
        c = atoms._get_constraints()
        indices_fixed=c[0].index    # the indices of atoms fixed
        for i in indices_fixed:
            f[i] = [0,0,0]
    except:
        pass
'''
out = open("./OUTCAR").readlines()
f, e = WriteForce(out)
index = [ i for i in range(len(e))]
headers = ['step', 'force', 'energy']
data = np.array([index, f, e])
data = list(zip(*data))
table = tabulate(data, headers, tablefmt = 'fancy_grid')
print(table)
