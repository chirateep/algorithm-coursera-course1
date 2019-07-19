# Uses python3
import sys


def optimal_weight(W, w):
    # write your code here
    value_array = list()

    for i in range(len(w) + 1):
        init_list = [float("-inf")] * (W + 1)
        value_array.append(init_list)

    for i in range(len(w) + 1):
        value_array[i][0] = 0

    for j in range(W + 1):
        value_array[0][j] = 0

    for i in range(1, len(w) + 1):
        for weight in range(1, W + 1):
            # print(i, weight)
            value_array[i][weight] = value_array[i - 1][weight]
            if (w[i - 1] <= weight):
                value = value_array[i - 1][weight - w[i - 1]] + w[i - 1]
                if value_array[i][weight] < value:
                    value_array[i][weight] = value

    # print(value_array)
    return value_array[len(w)][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
