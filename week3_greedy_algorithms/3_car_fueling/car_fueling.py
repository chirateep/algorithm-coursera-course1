# python3
import sys


def compute_min_refills(distance, tank, stops):
    full_tank = tank
    current_distance = 0
    num_stop = 0
    stops.append(distance)
    index_stop = 0
# 200 375 550 750
    while (tank > 0):
        # print(tank)
        next_spent_fuel = stops[index_stop + 1] - stops[index_stop]
        spent_fuel = stops[index_stop] - current_distance
        if (tank - spent_fuel) >= 0:
            tank -= spent_fuel

        if next_spent_fuel > tank:
            num_stop += 1
            tank = full_tank

        if next_spent_fuel > full_tank:
            return -1

        current_distance = stops[index_stop]
        index_stop += 1
        if index_stop == (len(stops) - 1):
            break

    return num_stop


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
