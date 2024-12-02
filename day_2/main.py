"""
https://adventofcode.com/2024/day/2
"""


def parse_input(s: str):
    out = []
    for line in s.strip().split("\n"):
        items = line.split(" ")
        items = [int(i) for i in items]
        out.append(items)

    return out


def part1(s: str) -> int:
    reports = parse_input(s)
    count = 0
    for report in reports:
        tmp = []
        for i in range(1, len(report)):
            tmp.append(report[i] - report[i - 1])

        if all([3 >= i >= 1 for i in tmp]) or all([-3 <= i <= -1 for i in tmp]):
            count += 1
    return count


# brute force all possible combinations
def part2(s: str) -> int:
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


if __name__ == "__main__":
    with open("input.txt") as f:
        INPUT = f.read()
    print(f"{part1(INPUT) = }")
    print(f"{part2(INPUT) = }")
