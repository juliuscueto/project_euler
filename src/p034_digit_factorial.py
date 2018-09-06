from math import factorial


def iscurious(num):
    num_original = num
    fact_sum = 0
    while num != 0:
        digit = num % 10
        fact_sum += factorial(digit)
        num = num // 10
    return (fact_sum == num_original) and (fact_sum not in [1, 2])


if __name__ == "__main__":
    i = 1
    while factorial(9)*i > 10**i - 1:
        i += 1
    max_digits = i

    curious_l = []
    for j in range(3, 10**max_digits):
        if iscurious(j):
            curious_l.append(j)
    print(curious_l)
    print(sum(curious_l))
