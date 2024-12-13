# https://adventofcode.com/2024/day/12

import collections

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Solution:
    def __init__(self):
        self.seen = set()
        self.areas = []
        self.perimeters = []
        self.fences = collections.defaultdict(list)
        self.price = 0

    def parse_input(self, s):
        return s.strip().split("\n")

    def iterate(self, s: list[list], y, x, prev, direction):
        if x < 0 or x >= len(s[0]) or y < 0 or y >= len(s):
            self.fences[(y - direction[0], x - direction[1])].append(direction)
            return 0, 1
        elif s[y][x] != prev:
            self.fences[(y - direction[0], x - direction[1])].append(direction)
            return 0, 1
        elif (y, x) in self.seen:
            return 0, 0

        a_ret = 1
        p_ret = 0
        self.seen.add((y, x))

        for i in DIRECTIONS:
            a_tmp, p_tmp = self.iterate(s, y + i[0], x + i[1], s[y][x], i)
            a_ret += a_tmp
            p_ret += p_tmp

        return a_ret, p_ret

    def calculate_total_edges(self, s, y, x, prev_fences, prev_fences_counted):
        fences_in_this_cell = self.fences[(y, x)]
        fence_edges = 0
        if (y, x) in self.seen:
            for i in DIRECTIONS:
                if i in prev_fences_counted and i in fences_in_this_cell:
                    fence_edges -= 1
            return fence_edges

        self.seen.add((y, x))

        fences_counted_prev_square = set()
        for i in DIRECTIONS:
            if i not in prev_fences and i in fences_in_this_cell:
                fence_edges += 1
                fences_counted_prev_square.add(i)

            if i not in fences_in_this_cell:
                fence_edges += self.calculate_total_edges(s, y + i[0], x + i[1], fences_in_this_cell, fences_counted_prev_square)

        return fence_edges

    def solve(self, s):
        s = self.parse_input(s)

        for idy in range(len(s)):
            for idx in range(len(s[0])):
                area, _ = self.iterate(s, idy, idx, s[idy][idx], (0, 0))
                self.areas.append(area)

        self.seen = set()

        for idy in range(len(s)):
            for idx in range(len(s[0])):
                perimeter = self.calculate_total_edges(s, idy, idx, [], set())
                print(perimeter)
                self.perimeters.append(perimeter)

        for i, j in zip(self.areas, self.perimeters):
            self.price += i * j

        return self.price


def solve(s):
    return Solution().solve(s)
