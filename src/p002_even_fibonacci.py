#!/usr/bin/env python
# -*- coding: utf-8 -*-

# learned about generators
import numpy as np

def fibs_generator(max):
    a = 1
    b = 2
    while a < max:
        yield a
        a, b = b, a + b

def fibs_generator_even(max):
    a = 1
    b = 2
    while a < max:
        if a%2 == 0:
            yield a
        a, b = b, a + b

if __name__ == "__main__":
    max = 4*10**6
    fibs = fibs_generator_even(max)
    print(np.sum(np.fromiter(fibs, int)))
