# https://adventofcode.com/2024/day/12


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Solution:
    def __init__(self):
        self.seen = set()
        self.price = 0

    def parse_input(self, s):
        return s.strip().split("\n")

    def iterate(self, s: list[list], y, x, prev):
        if x < 0 or x >= len(s[0]) or y < 0 or y >= len(s):
            return 0, 1
        elif s[y][x] != prev:
            return 0, 1
        elif (y, x) in self.seen:
            return 0, 0

        a_ret = 1
        p_ret = 0
        self.seen.add((y, x))

        for i in DIRECTIONS:
            a_tmp, p_tmp = self.iterate(s, y + i[0], x + i[1], s[y][x])
            a_ret += a_tmp
            p_ret += p_tmp

        return a_ret, p_ret

    def solve(self, s):
        s = self.parse_input(s)

        for idy in range(len(s)):
            for idx in range(len(s[0])):
                area, perimeter = self.iterate(s, idy, idx, s[idy][idx])
                self.price += area * perimeter

        return self.price


def solve(s):
    return Solution().solve(s)
