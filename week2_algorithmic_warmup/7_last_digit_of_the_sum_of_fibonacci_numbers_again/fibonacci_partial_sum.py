# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


def fibonacci_partial_sum_fast(from_, to):
    if to <= 1:
        return to

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

    mod_fib.pop()
    mod_fib.pop()

    from_mod = from_ % len(mod_fib)
    to_mod = to % len(mod_fib)

    index = from_mod
    sum = mod_fib[index]
    while(index >= 0):
        if index == 59:
            index = 0
        else:
            index += 1

        sum += mod_fib[index]

        if index == to_mod:
            break

    sum_digit = sum % 10

    sum_round = 0
    for i in range(len(mod_fib)):
        sum_round += i
    sum_round_digit = sum_round % 10

    digit = 0
    diff_window = to - from_
    round = int(diff_window / len(mod_fib))
    if round > 0:
        digit = ((sum_round_digit * round) + sum_digit) % 10
    else:
        digit = sum_digit

    return digit

if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    # print(fibonacci_partial_sum_naive(from_, to))
    print(fibonacci_partial_sum_fast(from_, to))
