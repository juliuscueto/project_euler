#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import itertools
import numpy as np
import sys


def is2_5mult(num):
    ret = False
    while num > 0 and not ret:
        tmp = num % 10
        num = num // 10
        ret |= (tmp % 2 == 0)
        ret |= (tmp % 5 == 0)
    return ret


def possible3mult(num):
    return num % 3 == 0


if __name__ == "__main__":
    sys.path.append("..")
    import eulerutil.util as util

    parser = argparse.ArgumentParser()
    parser.add_argument("num", type=int)
    args = parser.parse_args()

    p_l = util.primesfrom2to(args.num)
    red_p_l = p_l[np.logical_not(possible3mult(p_l))]
    mask = np.zeros_like(red_p_l, dtype=bool)
    for i, p in enumerate(red_p_l):
        mask[i] = not is2_5mult(p)
    red_p_l = red_p_l[mask]
    tried = []
    p_circ = [2, 3, 5]

    for p in red_p_l:
        if p not in tried:
            rots = []
            power = np.int(np.log10(p))
            prv = p
            for i in range(power+1):
                prv = prv // 10 + (prv % 10)*10**power
                rots.append(prv)
            # as_l = [x for x in str(p)]
            # rots = [
            #     as_l[n:] + as_l[:n] for n in range(len(as_l))]
            # rots = [int("".join(x)) for x in rots]
            is_circ = True
            for rot in rots:
                if rot not in p_l:
                    is_circ = False
                    break
            if is_circ:
                p_circ += rots
                p_circ = list(set(p_circ))
            tried += rots
            tried = list(set(tried))
    p_circ.sort()
    print(len(p_circ))
