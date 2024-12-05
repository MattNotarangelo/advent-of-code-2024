# https://adventofcode.com/2024/day/2


def parse_input(s):
    out = []
    for line in s.strip().split("\n"):
        items = line.split(" ")
        items = [int(i) for i in items]
        out.append(items)

    return out


# brute force all possible combinations
def solve(s):
    reports = parse_input(s)
    count = 0
    for report in reports:
        if check_report(report):
            count += 1
        else:
            for i in range(len(report)):
                if check_report(report[:i] + report[i + 1 :]):
                    count += 1
                    break

    return count


def check_report(report):
    tmp = []
    for i in range(1, len(report)):
        tmp.append(report[i] - report[i - 1])

    return all([3 >= i >= 1 for i in tmp]) or all([-3 <= i <= -1 for i in tmp])
