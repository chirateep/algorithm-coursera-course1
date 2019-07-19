# Uses python3
import sys

major_list = dict()
major_list[-1] = 0


def get_majority_element(a, left, right):
    # print(left, right)
    if left == right:
        return -1
    if left + 1 == right:
        if a[left] in major_list:
            major_list[a[left]] += 1
        else:
            major_list[a[left]] = 1
        return a[left]

    mid = (left + right) // 2
    major_left = get_majority_element(a, left, mid)
    major_right = get_majority_element(a, mid, right)

    # print("compare", major_left, major_right)
    # print(major_list)

    major = -1
    if major_left == major_right:
        major = major_left
    else:
        if major_list[major_left] > major_list[major_right]:
            major = major_left
        elif major_list[major_left] == major_list[major_right]:
            major = -1
        elif major_list[major_left] < major_list[major_right]:
            major = major_right

    # print('major', major)
    # print('greater', (right - left) / 2)
    if major_list[major] > (right - left) / 2:
        return major
    else:
        return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
