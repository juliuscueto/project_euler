#!/usr/bin/env python
# -*- coding: utf-8 -*-


def isDoublePalin(n):
    palin_dec = int("".join(list(str(n))[::-1]))
    palin_bin = "0b"+bin(n)[2:][::-1]
    return (n == palin_dec) and (bin(n) == palin_bin)


if __name__ == "__main__":
    import numpy as np
    doublePalin = []
    for i in np.arange(1, 10**6, 2):
        if isDoublePalin(i):
            doublePalin.append(i)
    print(doublePalin)
    print(sum(doublePalin))
