# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge_fast(n, m):
    if n <= 1:
        return n

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

    index = n % counter
    return mod_fib[index]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    # print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge_fast(n, m))
