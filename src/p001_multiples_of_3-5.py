import numpy as np

if __name__ == "__main__":
    l = np.arange(1000)
    l_3 = np.equal(l % 3, np.zeros_like(l))
    l_5 = np.equal(l % 5, np.zeros_like(l))
    l_15 = np.equal(l % 15, np.zeros_like(l))
    print(np.sum(l[np.logical_or(l_3, l_5)]))
