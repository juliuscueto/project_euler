import numpy as np

if __name__ == "__main__":
    tmp = np.arange(100, 1000)
    l = np.flip(np.unique(np.outer(tmp.T, tmp).flatten()), axis = 0)
    for i in l:
        if i == float(str(i)[::-1]):
            break
    print(i)
