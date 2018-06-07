#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def primesfrom2to(n):
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1, int(np.sqrt(n))//3+1):
        if sieve[i]:
            k = (3*i+1)|1
            sieve[k*k//3::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] =False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]

def approx_nth_prime(n):
    return n*(np.log(n)+np.log(np.log(n)) -1 + 1.8*np.log(np.log(n))/np.log(n))

# for n > 13
def nth_prime(n):
    approx_prime = int(np.ceil(approx_nth_prime(n)))
    l = primesfrom2to(approx_prime)
    if n <= len(l):
        return l[n-1]
    else:
        approx_prime = approx_nth_prime(n+1)
        l = primesfrom2to(approx_prime)
        return l[n-1]

if __name__ == "__main__":
    print(nth_prime(10001))
