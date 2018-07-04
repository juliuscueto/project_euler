import sys
import numpy as np
sys.path.append('../')

import eulerutil.util as util

def lex(_l,n):
    n = n-1
    l = _l.copy()
    num = len(l)
    fact = util.factorialto(num)
    ret = []
    itr = len(l) - 1
    while l:
        tmp = l.pop(int(n//fact[itr-1]))
        ret.append(tmp)
        n = n % fact[itr-1]
        itr = itr - 1
    return ret

if __name__ == "__main__":
    l = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print(''.join(lex(l,1000000)))
