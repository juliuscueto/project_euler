#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,numba,time
sys.path.append('../')

import numpy as np
import eulerutil.util as util

@numba.jit
def sumof_non_sumofabundant_under(limit):
    l_p = util.primesfrom2to(limit)
    l_a = util.abundantto(limit, l_p)
    l_ax, l_ay = np.meshgrid(l_a, l_a, sparse=True)
    possible_in_sum = np.unique(l_ax+l_ay)
    under_limit = possible_in_sum[possible_in_sum<limit]
    return np.sum(np.arange(limit)) - np.sum(under_limit)

if __name__ == "__main__":
    limit = 28123
    start_time = time.time()
    print(sumof_non_sumofabundant_under(limit))
    print("--- {} seconds ---".format(time.time() - start_time))
