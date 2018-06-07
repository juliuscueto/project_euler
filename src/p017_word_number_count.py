#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

import numpy as np
import eulerutil.util as util

class words(object):
    def __init__(self):
        self.order_one = util.elementlen(['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])

        self.order_ten = util.elementlen(['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'])

        self.order_tens = util.elementlen(['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',  'seventy', 'eighty', 'ninety'])

        self.order_suffix = util.elementlen(['', '', 'hundred', 'thousand'])

    def isunder100(self, n):
        ret = 0
        if n in range(20, 100, 1):
            ret = self.order_tens[n//10] + self.order_one[n%10]
        elif n in range(10, 20, 1):
            ret = self.order_ten[n%10]
        elif n in range(1, 10, 1):
            ret = self.order_one[n]
        else:
            ret = False
        return ret

    def leninword(self, n):
        assert n < 10000
        ans = 0
        while True:
            check = self.isunder100(n)
            if check or n == 0:
                ans += check
                break
            else:
                order = len(str(n)) - 1
                ans += self.order_suffix[order] + self.order_one[n//(10**order)]
                n = n%(10**order)
                if n != 0:
                    ans += 3
        return ans

if __name__ == "__main__":
    words = words()
    sum = 0
    for i in range(1, 1001, 1):
        sum += words.leninword(i)
    print(sum)
