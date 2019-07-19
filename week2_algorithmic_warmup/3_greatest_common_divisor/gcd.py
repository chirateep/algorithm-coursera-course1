# Uses python3
import sys


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_euclidean(a, b):
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

    return int(max_value)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # print(gcd_naive(a, b))
    print(gcd_euclidean(a, b))
