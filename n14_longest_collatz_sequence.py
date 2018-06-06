#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys

def collatz(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1

def longest_collatz_under(n):
    count_arr = np.zeros(n+1)
    for i in np.arange(1, n+1, 1):
        count = 1
        tmp = i
        while collatz(tmp) != 1:
            if tmp <= n:
                if count_arr[tmp] != 0:
                    count += count_arr[tmp]
                    break
            count += 1
            tmp = collatz(tmp)
        count_arr[i] = count
    return count_arr

if __name__ == "__main__":
    ret = longest_collatz_under(1000000)
    print(np.argmax(ret))
