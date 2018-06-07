#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

import numpy as np
import eulerutil.util as util

def factlistto(n):
    return np.cumprod(np.arange(1,n+1,1, dtype=np.float64))

if __name__ == '__main__':
    for x in util.fibs(10):
        print(x)
    list = factlistto(40)
    print(list)
    print(list[40-1]/(list[19]**2))
