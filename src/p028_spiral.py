import sys
import numpy as np
sys.path.append('../')

import eulerutil.util as util

class SpiralDiagsum(object):
    def __init__(self,N):
        self.N = N

    def returnsum(self):
        sum = 1
        for i in np.arange(1,self.N,2):
            sum += self.spiralsum(i)
        return sum

    def spiralsum(self,n):
        tmp = np.arange(n**2+1,(n+2)**2+1)
        k = int(len(tmp)/4)
        return np.sum(tmp[k-1::k])

if __name__ == "__main__":
    test = SpiralDiagsum(1001)
    print(test.returnsum())
