import sys
import numpy as np
sys.path.append('../')

import eulerutil.util as util

if __name__ == "__main__":
    itr = 2
    for fib in util.fibs(10**1000):
        if fib >= 10**(1000-1):
            print(tmp//10**(1000-1))
            print(fib//10**(1000-1))
            break
        tmp = fib
        itr = itr + 1
    print(itr)
