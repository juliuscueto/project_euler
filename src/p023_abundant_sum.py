#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,numba,time
sys.path.append('../')

import numpy as np
import eulerutil.util as util

@numba.jit
def test(n, l_p):
    for i in range(2,n+1,1):
        util.isabundant(i, l_p)

if __name__ == "__main__":
    start_time = time.time()
    l_p = util.primesfrom2to(10000)
    test(10000,l_p)
    print("--- {} seconds ---".format(time.time() - start_time))
