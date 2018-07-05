import sys
import numpy as np
sys.path.append('../')

import eulerutil.util as util

def indecimal(_n,_d):
    ret = []
    mod_list = []
    decimal_flag = False
    n = _n
    d = _d
    while True:
        ret.append(str(int(n//d)))
        if n < d and not decimal_flag:
            ret.append(".")
            decimal_flag = True
        if n%d == 0:
            break
        if n%d in mod_list:
            ret.append("...")
            break
        mod_list.append(n%d)
        n = n%d * 10

    return ret

def longest_rec_to(n):
    ind_d = 1
    len_d = 0
    for i in range(1,n,1):
        tmp = indecimal(1,i)
        if "..." in tmp:
            if (len(tmp)-2) > len_d:
                ind_d = i
                len_d = len(tmp)-2
    return(ind_d)

def indecimal_wrapper(_n,_d):
    return "".join(indecimal(_n,_d))

if __name__ == "__main__":
    print(longest_rec_to(1000))
