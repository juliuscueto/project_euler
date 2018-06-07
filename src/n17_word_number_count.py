#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

import numpy as np
import eulerutil.util as util

class leninwords(object):
    self.one_digit = util.elementlen(['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])

    self.order_ten = util.elementlen(['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'])

    self.order_tens = util.elementlen(['twenty', 'thirty', 'forty', 'fifty', 'sixty',  'seventy', 'eighty', 'ninety'])

    self.order = util.elementlen(['', '', 'hundred', 'thousand'])

    def wordlen(self, n):
        assert n < 10000:
        # TODO: organize condition
        if n == 0:
            ret = 4
            return ret

        if n % 1000 == 0:
            ret += self.order[3]
            if n // 1000 in range(1,10,1):
                ret += self.one_digit(n//1000)



    def sumofdigit(self, num):
    return np.sum(util.num_to_arr(num))




if __name__ == "__main__":
    print(util.elementlen(one_digit))
