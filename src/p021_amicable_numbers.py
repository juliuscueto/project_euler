#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

import eulerutil.util as util
import numpy as np

def sumto(n, a):
    return (a**(n+1)-1)/(a-1)

def sumoffactor(n, l_p = False):
    if l_p.any():
        l_p = l_p
    else:
        l_p = util.primesfrom2to(n)
    l_f = util.factor(n, l_p)
    ret = 1
    for i in range(len(l_f)):
        if l_f[i]:
            ret *= sumto(l_f[i], l_p[i])
    return ret - n

def amicablein(n, l_p = False, perfect=False):
    if l_p.any():
        l_p = l_p
    else:
        l_p = util.primesfrom2to(n)
    nums = np.arange(2, n+1, 1, dtype=int)
    check = np.ones_like(nums, dtype=bool)
    ret = np.zeros_like(nums, dtype=bool)
    for i in range(len(check)):
        sys.stdout.write("\ri:{0:5d}".format(i))
        sys.stdout.flush()
        if check[i] == True:
            pair = sumoffactor(nums[i], l_p)
            if pair <= 10000:
                tmp = sumoffactor(pair, l_p)
                if tmp == nums[i] and (perfect or not pair == tmp):
                    sys.stdout.write("\rpair {0:5d}, {1:5d}\n".format(int(pair), int(tmp)))
                    sys.stdout.flush()
                    ret[i] = True
                    ret[int(pair)-2] = True
                check[i] = False
                check[int(pair)-2] = False
    return nums[ret]

if __name__ == '__main__':
    primes = util.primesfrom2to(10000)
    print("\rsum of amicables:{}".format(np.sum(amicablein(10000, primes))))
