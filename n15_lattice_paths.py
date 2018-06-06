#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def factlistto(n):
    return np.cumprod(np.arange(1,n+1,1, dtype=np.float64))

if __name__ == '__main__':
    list = factlistto(40)
    print(list)
    print(list[40-1]/(list[19]**2))
