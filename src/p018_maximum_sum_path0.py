#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,time
sys.path.append('../')

import numpy as np
import eulerutil.util as util

class trianglepath(object):
    def __init__(self, triangle):
        self.l = [np.fromstring(line.lstrip(), dtype=int, sep=' ') for line in reversed(triangle.splitlines()) if line.lstrip()]

    def maxpathsum(self):
        for i in range(len(self.l)):
            tmp = self.l[i]
            comp = np.r_[0,tmp[:len(tmp)-1]]
            max = np.maximum(tmp, comp)[1:]
            if i < len(self.l) - 1:
                self.l[i+1] += max
        return self.l[len(self.l)-1][0]

if __name__ == "__main__":
    triangle = """
    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    """

    large_triangle = """
    """
    start_time = time.time()
    test = trianglepath(triangle)
    print(test.maxpathsum())
    print("--- {} seconds ---".format(time.time() - start_time))
