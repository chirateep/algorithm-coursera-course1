# Uses python3

import sys
import pprint


def lcs3(a, b, c):
    # write your code here
    n = len(a)
    m = len(b)
    o = len(c)
    max_common = list()

    for i in range(n + 1):
        slide_list = list()
        for j in range(m + 1):
            init_list = [float("-inf")] * (o + 1)
            slide_list.append(init_list)
        max_common.append(slide_list)

    for i in range(n + 1):
        for j in range(m + 1):
            max_common[i][j][0] = 0

    for j in range(m + 1):
        for k in range(o + 1):
            max_common[0][j][k] = 0

    for k in range(o + 1):
        for i in range(n + 1):
            max_common[i][0][k] = 0

    # pprint.pprint(max_common)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, o + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    diff = 1
                else:
                    diff = 0
                max_common[i][j][k] = max(max_common[i][j][k - 1],
                                          max_common[i][j - 1][k],
                                          max_common[i][j - 1][k - 1],
                                          max_common[i - 1][j][k],
                                          max_common[i - 1][j][k - 1],
                                          max_common[i - 1][j - 1][k],
                                          max_common[i - 1][j - 1][k - 1] + diff)

    # pprint.pprint(max_common)

    return max_common[n][m][o]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
