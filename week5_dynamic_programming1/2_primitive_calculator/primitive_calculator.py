# Uses python3
import sys


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def dp_optimal_sequence(n):
    min_num_opt = [n + 1] * (n + 1)
    map_otp_seq = dict()
    operations = ["+1", "*2", "*3"]

    min_num_opt[1] = 0
    map_otp_seq[1] = [1]

    for i in range(2, n + 1):
        for opt in operations:
            opt_i = operate_i(i, opt)
            min_opt = min_num_opt[opt_i] + 1
            if min_opt < min_num_opt[i]:
                min_num_opt[i] = min_opt
                map_otp_seq[i] = map_otp_seq[opt_i][:]
                map_otp_seq[i].append(i)
        # print(min_num_opt)
        # print(map_otp_seq)
    # print(map_otp_seq)
    return map_otp_seq[n]


def operate_i(i, opt):
    if opt == "*2" and i % 2 == 0:
        return i // 2
    elif opt == "*3" and i % 3 == 0:
        return i // 3

    return i - 1


input = sys.stdin.read()
n = int(input)
sequence = list(dp_optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
