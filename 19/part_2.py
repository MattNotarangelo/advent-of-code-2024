# https://adventofcode.com/2024/day/19

import collections


class Solution:
    def __init__(self):
        self.patterns = []
        self.to_check = []
        self.paths = set()
        self.mem = collections.defaultdict(list)

    def parse_input(self, s):
        s = s.split("\n\n")
        self.patterns = s[0].split(", ")
        self.to_check = s[1].split("\n")

    def iterate(self, pattern, to_check, paths):
        if to_check == "":
            self.paths.add(tuple(paths))
            return []
        ret = []
        for i in range(len(pattern)):
            if pattern[i] == to_check[: len(pattern[i])]:
                if to_check[len(pattern[i]) :] in self.mem:
                    for i in
                else:
                    ret.append([pattern[i]] + self.iterate(pattern, to_check[len(pattern[i]) :], paths[:] + [pattern[i]]))

    def solve(self, s):
        self.parse_input(s)

        for i in self.to_check:
            print("checking", i)
            self.iterate(self.patterns, i, [])
        return len(self.paths)


def solve(s):
    return Solution().solve(s)
