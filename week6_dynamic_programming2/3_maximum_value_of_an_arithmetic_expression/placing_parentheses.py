# Uses python3
import pprint


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(dataset):
    # write your code here
    m = list()
    M = list()
    n = (len(dataset) + 1) // 2

    for i in range(n + 1):
        init_list = [float("-inf")] * (n + 1)
        M.append(init_list[:])
        m.append(init_list[:])

    for i in range(1, len(dataset) + 1, 2):
        index = (i + 1) // 2
        m[index][index] = int(dataset[i - 1])
        M[index][index] = int(dataset[i - 1])

    # pprint.pprint(m)
    # pprint.pprint(M)
    for s in range(1, n):
        # print(s)
        for i in range(1, (n + 1) - s):
            j = i + s
            # print(i, s, j)
            min_val = float("inf")
            max_val = float("-inf")
            for k in range(i, j):
                op_index = ((k - 1) * 2) + 1
                # print(op_index)
                op = dataset[op_index]
                # print(op)
                # print(i, k, j)
                a = evalt(M[i][k], M[k + 1][j], op)
                # print(a)
                b = evalt(M[i][k], m[k + 1][j], op)
                # print(b)
                c = evalt(m[i][k], M[k + 1][j], op)
                # print(c)
                d = evalt(m[i][k], m[k + 1][j], op)
                # print(d)
                min_val = min(min_val, a, b, c, d)
                max_val = max(max_val, a, b, c, d)
                # print('max', max_val)
                # print('min', min_val)
            m[i][j] = min_val
            # pprint.pprint(m)
            # pprint.pprint(M)
            M[i][j] = max_val
            # pprint.pprint(m)
            # pprint.pprint(M)
            
    return M[1][n]


if __name__ == "__main__":
    print(get_maximum_value(input()))
