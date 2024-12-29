# https://adventofcode.com/2024/day/23

import networkx as nx


class Solution:
    def __init__(self):
        self.g = nx.Graph()

    def parse_input(self, s):
        s = s.strip().split("\n")
        for i in s:
            matches = i.split("-")
            if not self.g.has_node(matches[0]):
                self.g.add_node(matches[0])
            if not self.g.has_node(matches[1]):
                self.g.add_node(matches[1])
            self.g.add_edge(matches[0], matches[1])

    def solve(self, s):
        self.parse_input(s)
        max_clique = max(nx.find_cliques(self.g), key=len)
        return ",".join(sorted(max_clique))


def solve(s):
    return Solution().solve(s)
