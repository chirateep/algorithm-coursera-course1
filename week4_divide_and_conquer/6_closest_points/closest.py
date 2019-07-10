# Uses python3
import sys
import math


def fast_minimum_distance(x, y):
    pair = list()
    for i in range(len(x)):
        pair.append((x[i], y[i]))
    pair.sort()
    left = min(x)
    right = max(x)

    min_distance = recursive_minimum_distance(pair, left, right)
    return min_distance


def recursive_minimum_distance(pair, left, right):
    min_distance = 0
    if (right - left) <= 1:
        
        return distance(pair[left], pair[right])
    mid = (left + right) // 2
    min_distance_left = recursive_minimum_distance(pair, left, mid)
    min_distance_right = recursive_minimum_distance(pair, mid, right)

    print(min_distance_left)
    print(min_distance_right)
    min_distance = min(min_distance_left, min_distance_right)
    return min_distance


def naive_minimum_distance(x, y):
    # write your code here
    pair_list = list()
    for i in range(len(x)):
        pair_xy = (x[i], y[i])
        pair_list.append(pair_xy)
    # pair_list.sort()
    # print(pair_list)
    distance_list = list()
    for i in range(len(pair_list)):
        for j in range(i+1, len(pair_list)):
            dist = distance(pair_list[i], pair_list[j])
            distance_list.append(dist)
            # print(pair_list[i], pair_list[j], dist)

    return min(distance_list)


def distance(x, y):
    dist = math.hypot(y[0]-x[0], y[1]-x[1])
    return dist


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(fast_minimum_distance(x, y)))
