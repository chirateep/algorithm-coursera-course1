# Uses python3
import sys
import math


map_sort_y = dict()


def sort_y(pair):
    return pair[1]


def fast_minimum_distance(x, y):
    pair_sort_x = list()
    pair_sort_y = list()
    for i in range(len(x)):
        pair_sort_x.append((x[i], y[i]))
        pair_sort_y.append((x[i], y[i]))
    pair_sort_x.sort()
    pair_sort_y.sort(key=sort_y)

    for i in range(len(y)):
        map_sort_y[pair_sort_y[i]] = i

    # print(pair_sort_x)
    # print(pair_sort_y)

    left = 0
    right = len(pair_sort_x) - 1

    min_distance = recursive_minimum_distance(pair_sort_x, pair_sort_y,
                                              left, right)
    return min_distance


def recursive_minimum_distance(pair_sort_x, pair_sort_y, left, right):
    min_distance = 0
    if left == right:
        return min_distance
    if left + 1 == right:
        return distance(pair_sort_x[left], pair_sort_x[right])
    mid = (left + right) // 2
    min_distance_left = recursive_minimum_distance(pair_sort_x, pair_sort_y,
                                                   left, mid)
    min_distance_right = recursive_minimum_distance(pair_sort_x, pair_sort_y,
                                                    mid, right)

    min_distance = min(min_distance_left, min_distance_right)

    points_min_dist = list()
    x_mid = pair_sort_x[mid][0]

    for i in range(left, right):
        if x_mid - min_distance <= pair_sort_x[i][0] <= x_mid + min_distance:
            # index_point = map_sort_y[pair_sort_x[i]]
            points_min_dist.append(pair_sort_x[i])

    # print(points_min_dist)
    points_min_dist.sort(key=sort_y)
    for i in range(1, len(points_min_dist)):
        min_distance = min(min_distance, distance(points_min_dist[i],
                                                  points_min_dist[i-1]))

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
