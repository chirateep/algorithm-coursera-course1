# Uses python3
import sys
import random


def partition3(a, l, r):
    # print(a)
    x = a[l]
    less = list()
    equal = list()
    more = list()

    for i in range(l, r + 1):
        if a[i] < x:
            less.append(a[i])
        elif a[i] == x:
            equal.append(a[i])
        elif a[i] > x:
            more.append(a[i])

    m1 = len(less) + l
    m2 = m1 + len(equal) - 1
    full = less + equal + more
    a[l:r + 1] = full
    # print(m1, m2)
    return m1, m2


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, left, r):
    # print(a, l, r)
    if left >= r:
        return
    k = random.randint(left, r)
    a[left], a[k] = a[k], a[left]
    # use partition3
    m1, m2 = partition3(a, left, r)
    randomized_quick_sort(a, left, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
