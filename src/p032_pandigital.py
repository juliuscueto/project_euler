import itertools
import numpy as np
from functools import reduce

def noduplicatedigits(digit_l):
    return len(digit_l) == len(set(digit_l))

def ispermutation(digit_unused,num):
    if num in [tupletoint(j) for j in itertools.permutations(digit_unused)]:
        return True

def subset(a):
    for n in range(1,2**(len(a))):
        yield [a[i] for i in range(len(a)) if (n >> i) & 1 == 1]

def removefrom(a,b):
    return [x for x in a if x not in b]

def tupletoint(a):
    return reduce((lambda acc, x: acc*10 + x),a)

def searchpandigital(digits):
    validproducts = []
    for a in subset(digits):
        digit_not_a = removefrom(digits,a)
        if len(digit_not_a) > 1:
            for b in subset(digit_not_a):
                digit_unused = removefrom(digit_not_a,b)
                if len(digit_unused) > 0:
                    for comb_a in itertools.permutations(a):
                        for comb_b in itertools.permutations(b):
                            product = tupletoint(comb_a) * tupletoint(comb_b)
                            if ispermutation(digit_unused,product) and (product not in validproducts):
                                print(comb_a, comb_b, digit_unused, product)
                                validproducts.append(product)
    return validproducts

def main():
    digits = range(1,10)
    validproducts = searchpandigital(digits)
    ret = reduce((lambda acc, x: acc+x),validproducts)
    print(validproducts)
    print(ret)
    return 0

if __name__ == "__main__":
    main()
