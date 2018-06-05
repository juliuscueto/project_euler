import numpy as np

def primes(n):
    if n==2: l = [2]
    elif n<2: l = []
    s=np.arange(3,n+1,2)
    mroot = np.sqrt(n)
    half=len(s)
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=int((m*m-3)/2)
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    l = [2]+[x for x in s if x]
    return np.array(l)

if __name__ == '__main__':
    n = 600851475143
    l_p = primes(np.sqrt(n))
    factor = np.zeros_like(l_p)
    for i in range(len(l_p)):
        while n % l_p[i] == 0:
            n /= l_p[i]
            factor[i] += 1
        if n == 1:
            print(l_p[i])
            break
    print(np.prod(l_p**factor))
