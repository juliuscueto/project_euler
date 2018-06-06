import numpy as np

def primesfrom2to(n):
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1, int(np.sqrt(n))//3+1):
        if sieve[i]:
            k = (3*i+1)|1
            sieve[k*k//3::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] =False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]

def factor(n, primes=False):
    if primes:
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

def nth_triangle_number(n):
    return n*(n+1)//2

def num_of_divisor(n, primes=False):
    l_factor = factor(n, primes)
    return np.prod(l_factor[np.nonzero(l_factor)] + 1)

if __name__ == "__main__":
    i = 1
    primes = primesfrom2to(nth_triangle_number(1000000))
    while True:
        if num_of_divisor(nth_triangle_number(i), primes) > 500:
            ret = nth_triangle_number(i)
            break
        else:
            i += 1
    print(ret)
