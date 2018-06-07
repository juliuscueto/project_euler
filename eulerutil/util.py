#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def fibs(max):
    a = 1
    b = 2
    while a < max:
        yield a
        a, b = b, a+b

def primesfrom2to(n):
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1, int(np.sqrt(n))//3+1):
        if sieve[i]:
            k = (3*i+1)|1
            sieve[k*k//3::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] =False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]

def factor(n, primes=False):
    if primes.any():
        l_p = primes
    else:
        l_p = primesfrom2to(n)
    l = np.zeros_like(l_p)
    for i in range(len(l_p)):
        while n % l_p[i] == 0:
            n /= l_p[i]
            l[i] += 1
        if n == 1:
            break
    return l

def num_of_divisor(n, primes=False):
    l_factor = factor(n, primes)
    return np.prod(l_factor[np.nonzero(l_factor)] + 1)

def approx_nth_prime(n):
    return n*(np.log(n)+np.log(np.log(n)) -1 + 1.8*np.log(np.log(n))/np.log(n))

def nth_prime(n):
    approx_prime = int(np.ceil(approx_nth_prime(n)))
    l = primesfrom2to(approx_prime)
    if n <= len(l):
        return l[n-1]
    else:
        approx_prime = approx_nth_prime(n+1)
        l = primesfrom2to(approx_prime)
        return l[n-1]

def num_to_arr(num):
    return np.fromstring(str(num), np.int8) - 48

def str_to_mat(str, row, col):
    return np.fromstring(str, dtype=int, sep=' ').reshape(row, col)

def elementlen(list):
    return np.array([len(x) for x in list])
