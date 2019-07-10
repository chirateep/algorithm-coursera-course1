# Uses python3

import sys


def compare(digit, max_val):
    str_max_val = str(max_val)
    str_digit = str(digit)

    if int(str_max_val + str_digit) > int(str_digit + str_max_val):
        return False
    else:
        return True


def largest_number(a):
    res = ""

    while (len(a) > 0):
        max_val = 0
        for digit in a:
            if compare(digit, max_val):
                max_val = int(digit)
        # print(max_val)
        max_val = str(max_val)
        res += str(max_val)
        a.remove(max_val)
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
