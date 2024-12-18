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

    def parse_input(self, s):
        self.array = [list(i) for i in s.split("\n")]
        for y in range(len(self.array)):
            for x in range(len(self.array[0])):
                if self.array[y][x] == "S":
                    self.start = [x, y]
                if self.array[y][x] == "E":
                    self.end = [x, y]

    def bfs(self):

        # stack contains tuple of (x_pos, y_pos, direction, score, path)
        stack: collections.deque[tuple[int, int, tuple, int, list]] = collections.deque()
        stack.append((self.start[0], self.start[1], (1, 0), 0, []))
        seen = {}

        while len(stack) > 0:
            x, y, direction, score, path = stack.popleft()
            if self.array[y][x] == "#":
                continue
            if (x, y, direction) in seen and seen[(x, y, direction)] <= score:
                continue
            if score > self.min_score:
                continue

            if (x, y) == (self.end[0], self.end[1]):
                self.min_score = min(self.min_score, score)
                continue

            seen[(x, y, direction)] = score
            stack.append((x + direction[0], y + direction[1], direction, score + 1, path[:] + [(x, y)]))  # forward
            stack.append((x, y, MAP[direction]["L"], score + 1000, path[:]))  # rotate left
            stack.append((x, y, MAP[direction]["R"], score + 1000, path[:]))  # rotate left

    def solve(self, s):
        self.parse_input(s)

        self.bfs()
        return self.min_score


def solve(s):
    return Solution().solve(s)
