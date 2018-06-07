#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

if __name__ == "__main__":
    for a in range(1, 333):
        for b in range(a+1, (1000-a)//2):
            if a**2 + b**2 == (1000-a-b)**2:
                ret_a = a
                ret_b = b
    print(ret_a*ret_b*(1000-ret_a-ret_b))
