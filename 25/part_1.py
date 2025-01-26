# https://adventofcode.com/2024/day/


class Solution:
    def __init__(self):
        self.keys = []
        self.locks = []
        pass

    def parse_input(self, s):
        s = s.split("\n\n")
        for i in s:
            size = []
            cols = [list(j) for j in i.split("\n")]
            for z in zip(*cols):
                size.append(z.count("#") - 1)

            if self.is_lock(i):
                self.locks.append(size)
            else:
                self.keys.append(size)

    def is_lock(self, x):
        return all([i == "#" for i in x[0]])

    def solve(self, s):
        valids = 0

        self.parse_input(s)
        for i in self.keys:
            for j in self.locks:
                valid_case = True
                for x, y in zip(i, j):
                    if x + y > 5:
                        valid_case = False
                if valid_case:
                    valids += 1

        return valids


def solve(s):
    return Solution().solve(s)
