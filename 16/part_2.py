# https://adventofcode.com/2024/day/16
import collections

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
        self.array = []
        self.min_score = inf
        self.paths = collections.defaultdict(list)

    def parse_input(self, s):
        self.array = [list(i) for i in s.split("\n")]
        for y in range(len(self.array)):
            for x in range(len(self.array[0])):
                if self.array[y][x] == "S":
                    self.start = [x, y]
                if self.array[y][x] == "E":
                    self.end = [x, y]

    def bfs(self):

        #         x  y  d  s  path
        stack = [(self.start[0], self.start[1], (1, 0), 0, [])]
        seen = {}

        while len(stack) > 0:
            x, y, direction, score, path = stack.pop(0)
            if self.array[y][x] == "#":
                continue
            if (x, y, direction) in seen and seen[(x, y, direction)] < score:
                continue
            if score > self.min_score:
                continue

            if (x, y) == (self.end[0], self.end[1]):
                if score <= self.min_score:
                    self.min_score = score
                    self.paths[score].append(path)

                continue

            seen[(x, y, direction)] = score
            print(x, y, direction)
            stack.append((x + direction[0], y + direction[1], direction, score + 1, path[:] + [(x, y)]))  # forward
            stack.append((x, y, MAP[direction]["L"], score + 1000, path[:]))  # rotate left
            stack.append((x, y, MAP[direction]["R"], score + 1000, path[:]))  # rotate left

    def solve(self, s):
        self.parse_input(s)

        self.bfs()
        path_set = set()
        for path in self.paths[self.min_score]:
            for i in path:
                path_set.add(tuple(i))
        return len(path_set) + 1


def solve(s):
    return Solution().solve(s)
