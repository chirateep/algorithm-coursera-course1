# Uses python3

import sys


def lcs2(a, b):
    # write your code here
    n = len(a)
    m = len(b)
    max_common = list()

    for i in range(n + 1):
        init_list = [float("-inf")] * (m + 1)
        max_common.append(init_list)

    for i in range(n + 1):
        max_common[i][0] = 0

    for j in range(m + 1):
        max_common[0][j] = 0

    # print(max_common)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                diff = 1
            else:
                diff = 0
            max_common[i][j] = max(max_common[i - 1][j],
                                   max_common[i][j - 1],
                                   max_common[i - 1][j - 1] + diff)

    return max_common[n][m]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
