# https://adventofcode.com/2024/day/

import re


class Solution:
    def __init__(self):
        self.m = {}
        self.conns = []

    def parse_input(self, s):
        s = s.split("\n\n")
        for i in s[0].split("\n"):
            a, b = i.split(": ")
            self.m[a] = b
        for i in s[1].split("\n"):
            src, dest = i.split(" -> ")
            self.conns.append((src, dest))
        pass

    def perform_operation(self, a, b, operator):
        if operator == "AND":
            return int(a) & int(b)
        if operator == "OR":
            return int(a) | int(b)
        if operator == "XOR":
            return int(a) ^ int(b)
        raise ValueError("Invalid operator")

    def solve(self, s):
        self.parse_input(s)
        changed = True
        while changed:
            changed = False
            for i in self.conns:
                src, dest = i
                matches = re.findall(r"(\w+) (AND|OR|XOR) (\w+)", src)[0]
                arg0 = matches[0]
                arg1 = matches[2]
                operator = matches[1]
                if arg0 in self.m and arg1 in self.m and dest not in self.m:
                    self.m[dest] = self.perform_operation(self.m[arg0], self.m[arg1], operator)
                    changed = True

        k = self.m.keys()
        k = [i for i in k if i.startswith("z")]
        k.sort()
        ret = ""
        for i in k:
            ret += str(self.m[i])
        return int(ret[::-1], 2)


def solve(s):
    return Solution().solve(s)
