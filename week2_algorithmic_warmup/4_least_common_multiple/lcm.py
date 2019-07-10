# Uses python3
import sys


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def lcm_euclidean(a, b):
    mod_value = 1
    max_value = 1

    if (a >= b):
        max_value = a
        mod_value = b
    else:
        max_value = b
        mod_value = a

    while (max_value > 1 and mod_value > 0):
        max_value, mod_value = mod_value, max_value % mod_value

    return int((a * b) / max_value)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # print(lcm_naive(a, b))
    print(lcm_euclidean(a, b))
