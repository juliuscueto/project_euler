#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

if __name__ == "__main__":
    namelist = open("../data/p022_names.txt","r")
    list = np.array([name.strip('"').lower() for name in namelist.read().split(",")])
    # idx = np.argsort(list)
    list_sort = np.sort(list)
    # score = np.array([np.sum(np.array([ord(c)-ord('a') + 1 for c in name])) for name in list])
    sorted_score = np.array([np.sum(np.array([ord(c)-ord('a') + 1 for c in name])) for name in list_sort])
    # print(list_sort[937], list[idx[937]], score[idx[937]], sorted_score[937])
    print(np.sum(np.multiply(sorted_score, np.arange(len(sorted_score))+1)))
