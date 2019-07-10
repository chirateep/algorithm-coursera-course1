# Uses python3
import sys


def new_fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)

    sort_list = list()

    for i in range(len(starts)):
        start_wkey = (starts[i], 'l')
        sort_list.append(start_wkey)
        end_wkey = (ends[i], 'r')
        sort_list.append(end_wkey)

    for i in range(len(points)):
        point_wkey = (points[i], 'p', i)
        sort_list.append(point_wkey)

    sort_list.sort()
    # print(sort_list)

    count_left = 0
    count_right = 0

    # 0 is value, 1 is key (l, p, r), 2 is iter point
    for item in sort_list:
        if item[1] == 'l':
            count_left += 1
        elif item[1] == 'r':
            count_right += 1
        elif item[1] == 'p':
            i = item[2]
            cnt[i] += count_left - count_right

    return cnt


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    # write your code here
    starts.sort()
    ends.sort()

    for i in range(len(points)):
        point = points[i]
        lower_starts = lower_start(starts, point)
        lower_ends = lower_end(ends, point)
        # print(lower_starts)
        # print(lower_ends)

        cnt[i] += len(lower_starts) - len(lower_ends)

    return cnt


def lower_start(a, x):
    lower = list()
    left, right = 0, len(a)

    if (a[left] > x):
        return lower

    if (a[right-1] <= x):
        return a

    while (left <= right):
        mid = (left + right) // 2

        if (a[mid] <= x):
            lower += a[left:mid+1]
            left = mid + 1
        else:
            right = mid - 1

    return lower


def lower_end(a, x):
    lower = list()
    left, right = 0, len(a)

    if (a[left] > x):
        return lower

    if (a[right-1] <= x):
        return a

    while (left <= right):
        mid = (left + right) // 2

        if (a[mid] < x):
            lower += a[left:mid+1]
            left = mid + 1
        else:
            right = mid - 1

    return lower


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    # use fast_count_segments
    cnt = new_fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
