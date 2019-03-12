import math
import numpy as np


def isRTruncPrime(n, l_p):
    ret = True
    while n != 0:
        if n not in l_p:
            ret = False
            break
        else:
            n = n//10
    return ret


def isLTruncPrime(n, l_p):
    ret = True
    while n != 0:
        if n not in l_p:
            ret = False
            break
        else:
            n = n % 10**(int(math.log10(n)))
    return ret


def isTruncPrime(n, l_p):
    rTrunc = isRTruncPrime(n, l_p)
    lTrunc = isLTruncPrime(n, l_p)
    return np.logical_and(rTrunc, lTrunc)


def isTruncCandidate(n):
    n_str = str(n)
    set_even = set(["0", "4", "6", "8"])
    return not bool(set_even & set(n_str))


if __name__ == "__main__":
    import sys
    sys.path.append("..")
    import eulerutil.util as util

    N = 10**7
    l_p = util.primesfrom2to(N)
    l_withOutUnder10 = l_p[4:]
    l_slimmed = [x for x in l_withOutUnder10 if isTruncCandidate(x)]
    ret = []
    for n in l_slimmed:
        trunc_flag = isTruncPrime(n, l_p)
        print(n, trunc_flag)
        if trunc_flag:
            ret.append(n)
        if len(ret) == 11:
            break
    print(ret)
    print(sum(ret))
