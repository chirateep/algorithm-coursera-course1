# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0
    sorted_value_unit = []
    map_pos_sorted = dict()

    for i in range(len(weights)):
        value_unit = float(values[i]) / weights[i]
        sorted_value_unit.append(value_unit)
        map_pos_sorted[value_unit] = i

    # print(sorted_value_unit)
    sorted_value_unit.sort(reverse=True)
    # print(sorted_value_unit)
    # print(map_pos_sorted)

    index_item = 0
    while (capacity > 0):
        pos_item = map_pos_sorted[sorted_value_unit[index_item]]
        unit = min(weights[pos_item], capacity)
        item_value = sorted_value_unit[index_item] * unit
        # print(pos_item)
        # print(item_value)

        if (capacity - unit) >= 0:
            capacity -= unit
            value += item_value
            index_item += 1
            if index_item == n:
                break

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
