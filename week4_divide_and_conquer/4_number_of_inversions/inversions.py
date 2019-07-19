# Uses python3
import sys


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    # write your code here
    left_half = a[left:ave]
    right_half = a[ave:right]
    index_result = left
    while (len(left_half) > 0 and len(right_half) > 0):
        if left_half[0] <= right_half[0]:
            a[index_result] = left_half.pop(0)
        else:
            number_of_inversions += 1 * len(left_half)
            a[index_result] = right_half.pop(0)
        index_result += 1
    if len(left_half) == 0:
        a[index_result:right] = right_half
    else:
        a[index_result:right] = left_half

    # print(a)
    # print("num", number_of_inversions)
    return number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
