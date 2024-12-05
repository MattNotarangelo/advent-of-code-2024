"""
https://adventofcode.com/2024/day/3
"""

import re


def solve(s: str) -> int:
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
