import sys
import numpy as np
sys.path.append('../')

import eulerutil.util as util

def unique_power(a,b):
    a_l = np.arange(2,a+1,dtype=object)
    b_l = np.arange(2,b+1,dtype=object)
    aa, bb = np.meshgrid(a_l,b_l)
    return np.unique(aa**bb,return_counts=True)

if __name__ == "__main__":
    a = 100
    b = 100
    l,c = unique_power(a,b)
    print(c)
    print(len(c))
    print("sum of unique is: {}".format(np.sum(l)))
