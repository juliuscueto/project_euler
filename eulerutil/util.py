#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import numba


# basic operations
@numba.jit
def num_to_arr(num):
    return np.fromstring(str(num), np.int8) - 48


@numba.jit
def str_to_mat(str, row, col):
    return np.fromstring(str, dtype=int, sep=' ').reshape(row, col)


@numba.jit
def elementlen(list):
    return np.array([len(x) for x in list])


# basic series
def fibs(max):
    a = 1
    b = 2
    while a < max:
        yield a
        a, b = b, a+b


@numba.jit
def factorialto(n):
    toN = np.arange(1, n+1, 1)
    return np.cumprod(toN, dtype=np.float64)


# prime related functions

# prime generation
# @numba.jit
def primesfrom2to(n):
    """return array of primes up to n"""
    sieve = np.ones(n//3 + (n % 6 == 2), dtype=np.bool)
    for i in range(1, int(np.sqrt(n))//3+1):
        if sieve[i]:
            k = (3*i+1) | 1
            sieve[k*k//3::2*k] = False
            sieve[k*(k-2*(i & 1)+4)//3::2*k] = False
    return np.r_[2, 3, ((3*np.nonzero(sieve)[0][1:]+1) | 1)]


@numba.jit
def approx_nth_prime(n):
    return n*(np.log(n)
              + np.log(np.log(n)) - 1 + 1.8*np.log(np.log(n))/np.log(n))


@numba.jit
def nth_prime(n):
    approx_prime = int(np.ceil(approx_nth_prime(n)))
    p_l = primesfrom2to(approx_prime)
    if n <= len(p_l):
        return p_l[n-1]
    else:
        approx_prime = approx_nth_prime(n+1)
        p_l = primesfrom2to(approx_prime)
        return p_l[n-1]


# use factors
@numba.jit
def factor(n, l_p):
    """for given array of primes, count how many of each are factors of n"""
    z_l = np.zeros_like(l_p)
    for i in range(len(l_p)):
        while n % l_p[i] == 0 and n != 1:
            n /= l_p[i]
            z_l[i] += 1
    return z_l


@numba.jit
def num_of_divisor(n, primes=False):
    """return number of factors"""
    l_factor = factor(n, primes)
    return np.prod(l_factor[np.nonzero(l_factor)] + 1).astype(int)


@numba.jit
def sumto(n, a):
    return (a**(n+1)-1)/(a-1)


@numba.jit
def sumoffactor(n, l_p):
    l_f = factor(n, l_p)
    ret = 1
    for i in range(len(l_f)):
        ret *= sumto(l_f[i], l_p[i])
    return int(ret - n)


@numba.jit
def isabundant(n, l_p):
    return sumoffactor(n, l_p) > n


@numba.jit
def abundantto(n, l_p):
    tmp_l = [x for x in np.arange(12, n+1, 1) if isabundant(x, l_p)]
    return np.array(tmp_l)
