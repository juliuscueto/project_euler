#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

import numpy as np

class gausscalendar(object):
    def __init__(self, year, month, date):
        if month in np.arange(1,3):
            self.Y = year - 1
            self.m = month + 10
        else:
            self.Y = year
            self.m = month - 2
        self.y = self.Y % 100
        self.c = self.Y // 100
        self.d = date
        self.get_w()


    def get_w(self):
        ret = (1 + np.floor(2.6*self.m - 0.2) + self.y + np.floor(self.y/4) + np.floor(self.c/4) - 2*self.c)%7
        if ret < 0:
            ret += 7
        self.w = int(ret)

    def print_date(self, verbose = False):
        dates = ['Sunday', 'Monday', 'Tuesday', 'Thirsday', 'Wednesday', 'Friday', 'Saturday']
        dates_num = np.arange(0,7)
        if verbose:
            l = dates
        else:
            l = dates_num
        return l[self.w]

if __name__ == "__main__":
    count = 0
    for year in range(1901, 2001, 1):
        for month in range(1, 13, 1):
            date = gausscalendar(year, month, 1)
            if date.print_date() == 0:
                count += 1
    print(count)
