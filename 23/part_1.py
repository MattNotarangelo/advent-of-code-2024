# https://adventofcode.com/2024/day/23

import collections
import itertools


class Solution:
    def __init__(self):
        self.g = collections.defaultdict(set)
        self.seen = set()
        pass

    def parse_input(self, s):
        s = s.strip().split("\n")
        for i in s:
            matches = i.split("-")
            self.g[matches[0]].add(matches[1])
            self.g[matches[1]].add(matches[0])

    def solve(self, s):
        self.parse_input(s)
        sets = set()
        for i in self.g:
            for j in self.g:
                for k in self.g:
                    if i != j and i != k and j != k:
                        if i in self.g[j] and i in self.g[k] and j in self.g[k]:
                            sets.add(tuple(sorted([i, j, k])))
        sets_of_three = []
        for i in sets:
            sets_of_three.extend(itertools.combinations(i, 3))

        sets_of_three = [i for i in sets_of_three if i[0].startswith("t") or i[1].startswith("t") or i[2].startswith("t")]
        return len(sets_of_three)


def solve(s):
    return Solution().solve(s)
