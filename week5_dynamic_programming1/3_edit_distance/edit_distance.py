# Uses python3
def edit_distance(s, t):
    # write your code here
    n = len(s)
    m = len(t)
    min_edit_array = list()

    for i in range(n + 1):
        init_list = [float("inf")] * (m + 1)
        min_edit_array.append(init_list)

    for i in range(n + 1):
        min_edit_array[i][0] = i

    for j in range(m + 1):
        min_edit_array[0][j] = j

    # print(min_edit_array)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                diff = 0
            else:
                diff = 1
            min_edit_array[i][j] = min(min_edit_array[i - 1][j] + 1,
                                       min_edit_array[i][j - 1] + 1,
                                       min_edit_array[i - 1][j - 1] + diff)

    return min_edit_array[n][m]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
