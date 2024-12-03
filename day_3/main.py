"""
https://adventofcode.com/2024/day/3
"""

import re


def parse_input(s: str) -> str:
    return s.strip()


def part1(s: str) -> int:
    s = parse_input(s)
    matches = re.findall(r"mul\(\d+\,\d+\)", s)
    res = 0
    for i in matches:
        mul_args = i[4:-1].split(",")
        res += int(mul_args[0]) * int(mul_args[1])
    return res


# brute force all possible combinations
def part2(s: str) -> int:
    s = parse_input(s)
    matches = re.findall(r"(mul\(\d+\,\d+\)|do\(\)|don't\(\))", s)
    res = 0
    state = True
    for i in matches:
        if i == "don't()":
            state = False
        elif i == "do()":
            state = True
        elif state:
            mul_args = i[4:-1].split(",")
            res += int(mul_args[0]) * int(mul_args[1])
    return res


if __name__ == "__main__":
    with open("input.txt") as f:
        INPUT = f.read()
    print(f"{part1(INPUT) = }")
    print(f"{part2(INPUT) = }")
