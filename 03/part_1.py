"""
https://adventofcode.com/2024/day/3
"""

import re


def solve(s: str) -> int:
    matches = re.findall(r"mul\(\d+\,\d+\)", s)
    res = 0
    for i in matches:
        mul_args = i[4:-1].split(",")
        res += int(mul_args[0]) * int(mul_args[1])
    return res
