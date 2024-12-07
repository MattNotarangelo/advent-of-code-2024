# https://adventofcode.com/2024/day/7
import sys


def parse_input(s):
    ret = []
    rows = s.strip().split("\n")
    for row in rows:
        key, val = row.split(": ")
        key = int(key)
        ret.append((key, list(map(int, val.split(" ")))))
    return ret


def deep_copy(row):
    key, val = row
    return (key, val[:])


def check_valid(row, idx, cumsum):
    key, val = deep_copy(row)

    if cumsum == key and idx == len(val):
        return True
    elif cumsum != int(cumsum):
        return False
    elif cumsum > key or idx >= len(val):
        return False

    targets = [check_valid((key, val), idx + 1, cumsum + val[idx]), check_valid((key, val), idx + 1, int(str(cumsum) + str(val[idx])))]

    # since initial starting cumsum is 0, you can cheese the first element by multiplying by 0. Shouldn't be allowed
    if idx != 0:
        targets.append(check_valid((key, val), idx + 1, cumsum * val[idx]))

    return any(targets)


def solve(s):
    res = 0
    s = parse_input(s)
    for i in s:
        if check_valid(i, 0, 0):
            res += i[0]
    return res
