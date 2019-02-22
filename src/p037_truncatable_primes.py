import math
import numpy as np

def isRTruncPrime(n, l_p):
    ret = True
    while n != 0:
        if n not in l_p:
            ret = False
            break
        else:
            n == n/10
    return ret

def isLTruncPrime(n, l_p):
    while n != 0:
        if n not in l_p:
            ret = False
            break
        else:
            n == n%10**(int(math.log10(n)))
    return ret

def isTruncPrime(n, l_p):
    rTrunc = isRTruncPrime(n, l_p)
    lTrunc = isLTruncPrime(n, l_p)
    return np.logical_and(rTrunc, lTrunc)

if __name__ == "__main__":
    import sys
    sys.path.append("..")
    import eulerutil.util as util

    N = 10**7
    _n = util.nth_prime(N)
    l_p = util.primesfrom2to(_n)
    l_p = l_p[4:]
    ret = []
    for n in l_p:
        trunc_flag = isTruncPrime(n, l_p)
        print(n, trunc_flag)
        if trunc_flag:
            ret.append(n)
        if len(n) == 7:
            break
    print(ret)
    print(sum(ret))
