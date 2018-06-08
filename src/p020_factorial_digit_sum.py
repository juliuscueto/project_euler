#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

import numpy as np
import eulerutil.util as util

if __name__ == '__main__':
    n = 100
    num = util.factorialto(n)[n-1]
    dig = np.ceil(np.log10(num+1))
    l = np.r_[1, np.zeros(int(dig)-1)]
    for i in range(1,n+1):
        l = l*i
        for a in range(len(l)):
            if l[a] > 9:
                tmp = l[a]
                l[a] = tmp % 10
                l[a+1] += tmp // 10
    print(np.sum(l))
