import sys
import numpy as np
sys.path.append('../')

import eulerutil.util as util

class Quadratic(object):
    def __init__(self,max_p,a,b):
        self.primelist = util.primesfrom2to(max_p)
        print("finished making primes")
        a_l = np.arange(-a+1,a)
        b_tmp = np.arange(0,b+1)
        b_mask = np.isin(b_tmp, self.primelist)
        b_l = b_tmp[b_mask]
        self.a, self.b = np.meshgrid(a_l,b_l)

    def search_best(self):
        count = np.zeros_like(self.a,dtype=bool)
        n = 0
        step = self.quadratic_check(n)
        while step.any():
            n += 1
            sys.stdout.write("\r\u001b[0Kn={}".format(n))
            sys.stdout.flush()
            self.a = self.a[step]
            self.b = self.b[step]
            step = self.quadratic_check(n)
        print("\r\u001b[0Kfinished searching a:{}, b:{}".format(self.a,self.b))
        return self.a * self.b

    def quadratic_check(self,n):
        return np.isin(self.quadratic(n),self.primelist)

    def quadratic(self,n):
        return n**2 + self.a*n + self.b

    def showlist(self):
        print(self.a, self.b)

if __name__ == "__main__":
    test = Quadratic(1000000,1000,1000)
    print(test.search_best())
