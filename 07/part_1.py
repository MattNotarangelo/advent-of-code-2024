# https://adventofcode.com/2024/day/7


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
    if cumsum == key:
        return True
    elif cumsum != int(cumsum):
        return False
    elif cumsum > key or idx >= len(val):
        return False
    return check_valid((key, val), idx + 1, cumsum + val[idx]) or check_valid((key, val), idx + 1, cumsum * val[idx])


def solve(s):
    res = 0
    s = parse_input(s)
    for i in s:
        if check_valid(i, 0, 0):
            res += i[0]
    return res
