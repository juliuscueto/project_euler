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
    triangle_file = open('../data/p067_triangle.txt', 'r')
    triangle = triangle_file.read()
    start_time = time.time()
    test = trianglepath(triangle)
    print(test.maxpathsum())
    print("--- {} seconds ---".format(time.time() - start_time))
