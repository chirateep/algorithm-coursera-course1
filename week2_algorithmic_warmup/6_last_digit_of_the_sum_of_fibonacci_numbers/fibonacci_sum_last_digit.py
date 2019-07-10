# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fibonacci_sum_fast(n):
    if n <= 1:
        return n
    m = 10
    mod_fib = []

    previous = 0
    current = 1
    mod_fib.append(0)
    mod_fib.append(1)

    counter = 0

    previous, current = current % m, (previous + current) % m
    mod_fib.append(current)
    counter += 1

    while (previous != 0 or current != 1):
        previous, current = current % m, (previous + current) % m
        mod_fib.append(current)
        counter += 1

    len_fib = len(mod_fib) - 2
    sum = 0

    limiter = n % len_fib
    for digit in range(limiter + 1):
        sum += mod_fib[digit]

    sum_digit = sum % 10

    sum_round = 0
    for i in range(len_fib):
        sum_round += i
    sum_round_digit = sum_round % 10

    digit = 0
    round = int(n / len_fib)
    if round > 0:
        digit = ((sum_round_digit * round) + sum_digit) % 10
    else:
        digit = sum_digit

    return digit

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    # print(fibonacci_sum_naive(n))
    print(fibonacci_sum_fast(n))
