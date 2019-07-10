# Uses python3
import sys


def get_change(m):
    total_coin = 0
    coin_list = [10, 5, 1]
    coin_index = 0
    while (m > 0):
        value_size = coin_list[coin_index]
        # print(m, value_size)
        if (m - value_size) >= 0:
            m -= value_size
            total_coin += 1
        else:
            coin_index += 1
            if coin_index == len(coin_list):
                # end of coin type
                break
    return total_coin


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
