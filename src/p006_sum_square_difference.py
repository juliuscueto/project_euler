import numpy as np

def sum_square_difference(n):
    tmp = np.arange(1, n+1)
    l = np.outer(tmp.T,tmp)
    return np.sum(l-np.diag(tmp**2))

if __name__ == "__main__":
    print(sum_square_difference(100))
