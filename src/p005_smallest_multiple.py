import numpy as np

def primes(n):
    if n==2: l = [2]
    elif n<2: l = []
    s=np.arange(3,n+1,2)
    mroot = n ** 0.5
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

def factor(n):
    l_p = primes(n)
    l = np.zeros_like(l_p)
    for i in range(len(l_p)):
        while n % l_p[i] == 0:
            n /= l_p[i]
            l[i] += 1
        if n == 1:
            break
    return l.tolist()

def fill_list_to_array(ll):
    lens = [len(l) for l in ll]      # only iteration
    maxlen = max(lens)
    arr = np.zeros((len(ll),maxlen),int)
    mask = np.arange(maxlen) < np.array(lens)[:,None]
    arr[mask] = np.concatenate(ll)
    return arr

def smallest_multiple(n):
    for i in range(len(n)):
        if i == 0:
            ll = [factor(n[i])]
        else:
            ll.append(factor(n[i]))
    arr = fill_list_to_array(ll)
    min_p = np.amax(arr, axis=0)
    return(np.prod(primes(n.max())**min_p))

if __name__ == "__main__":
    print(smallest_multiple(np.arange(1,40)))
