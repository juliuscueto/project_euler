import sys
import numpy as np
sys.path.append('../')

import eulerutil.util as util

def getdigit(n):
    return np.array([int(x) for x in str(n)])

def powerissum(n,p):
    return n == np.sum(getdigit(n)**p)

def maxlen(p):
    n = 1
    while n*9**p > 10**n-1:
        n += 1
    return n

if __name__ == "__main__":
    p = 5
    l = np.arange(10,10**maxlen(p))
    issum = np.array([x for x in l if powerissum(x,p)])
    print(np.sum(issum))
