# https://adventofcode.com/2024/day/16
import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(5000)

inf = float("inf")
MAP = {
    (1, 0): {"L": (0, -1), "R": (0, 1)},
    (-1, 0): {"L": (0, 1), "R": (0, -1)},
    (0, 1): {"L": (1, 0), "R": (-1, 0)},
    (0, -1): {"L": (-1, 0), "R": (1, 0)},
}


def move(position, direction):
    return [position[0] + direction[0], position[1] + direction[1]]


class Solution:
    def __init__(self):
        self.start = [-1, -1]
        self.end = [-1, -1]
        self.direction = (1, 0)
        self.seen = {}
        self.array = []
        self.min_score = inf

    def parse_input(self, s):
        self.array = [list(i) for i in s.split("\n")]
        for y in range(len(self.array)):
            for x in range(len(self.array[0])):
                if self.array[y][x] == "S":
                    self.start = [x, y]
                if self.array[y][x] == "E":
                    self.end = [x, y]

    def dfs(self, position, direction, score):
        if self.array[position[1]][position[0]] == "#":
            return
        if position == self.end:
            self.min_score = min(self.min_score, score)
            return

        tupled_pos = tuple(position)
        if tupled_pos in self.seen:
            if self.seen[tupled_pos] <= score:
                return
            else:
                self.seen[tupled_pos] = score
        else:
            self.seen[tupled_pos] = score

        self.dfs(move(position, direction), direction, score + 1)
        self.dfs(move(position, MAP[direction]["L"]), MAP[direction]["L"], score + 1001)  # rotate and move
        self.dfs(move(position, MAP[direction]["R"]), MAP[direction]["R"], score + 1001)  # rotate and move
        self.dfs(move(position, MAP[MAP[direction]["R"]]["R"]), MAP[MAP[direction]["R"]]["R"], score + 2001)  # rotate and move

    def solve(self, s):
        self.parse_input(s)

        self.dfs(self.start, self.direction, 0)
        return self.min_score


def solve(s):
    return Solution().solve(s)
