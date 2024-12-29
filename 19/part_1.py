# https://adventofcode.com/2024/day/19


class Solution:
    def __init__(self):
        self.patterns = []
        self.to_check = []

    def parse_input(self, s):
        s = s.split("\n\n")
        self.patterns = s[0].split(", ")
        self.to_check = s[1].split("\n")

    def iterate(self, pattern, to_check):
        if to_check == "":
            return True
        res = False
        for i in range(len(pattern)):
            if pattern[i] == to_check[: len(pattern[i])]:
                print(pattern[i], to_check)
                res = res or self.iterate(pattern, to_check[len(pattern[i]) :])
        return res

    def solve(self, s):
        self.parse_input(s)
        print(self.patterns)
        print(self.to_check)
        res = 0

        for i in self.to_check:
            if self.iterate(self.patterns, i):
                res += 1
        return res


def solve(s):
    return Solution().solve(s)
