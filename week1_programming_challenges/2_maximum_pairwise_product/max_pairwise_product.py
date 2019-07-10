# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product, numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_fast(numbers):
    n = len(numbers)
    index = 0
    for first_index in range(1, n):
        if numbers[first_index] > numbers[index]:
            index = first_index
    numbers[index], numbers[n-1] = numbers[n-1], numbers[index]

    index = 0
    for second_index in range(1, n-1):
        if numbers[second_index] > numbers[index]:
            index = second_index
    numbers[index], numbers[n-2] = numbers[n-2], numbers[index]

    max_product = numbers[n-2] * numbers[n-1]
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
