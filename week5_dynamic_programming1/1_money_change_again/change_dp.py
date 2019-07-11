# Uses python3
import sys


def get_change(m):
    # write your code here
    coins = [1, 3, 4]
    min_num_coin = [m + 1] * (m + 1)
    min_num_coin[0] = 0
    for i in range(1, m + 1):
        for coin in coins:
            if i >= coin:
                num_coins = min_num_coin[i - coin] + 1
            if num_coins < min_num_coin[i]:
                min_num_coin[i] = num_coins
        # print(min_num_coin)
    return min_num_coin[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
