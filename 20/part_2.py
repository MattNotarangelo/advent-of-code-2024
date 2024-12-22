# https://adventofcode.com/2024/day/16
import collections

inf = float("inf")
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Solution:
    def __init__(self):
        self.start = [-1, -1]
        self.end = [-1, -1]
        self.array = []
        self.score_map = {}

    def parse_input(self, s):
        self.array = [list(i) for i in s.split("\n")]
        for y in range(len(self.array)):
            for x in range(len(self.array[0])):
                if self.array[y][x] == "S":
                    self.start = [x, y]
                if self.array[y][x] == "E":
                    self.end = [x, y]

    def bfs(self):

        # stack contains tuple of (x_pos, y_pos, score)
        stack: collections.deque[tuple[int, int, int]] = collections.deque()
        stack.append((self.start[0], self.start[1], 0))
        seen = {}

        while len(stack) > 0:
            x, y, score = stack.popleft()
            if self.array[y][x] == "#":
                continue
            if (x, y) in seen and seen[(x, y)] < score:
                continue

            if (x, y) == (self.end[0], self.end[1]):
                seen[(x, y)] = score
                continue

            seen[(x, y)] = score

            for dx, dy in DIRECTIONS:
                stack.append((x + dx, y + dy, score + 1))

        self.score_map = seen

    def check(self, x, dx, y, dy, score):
        x += dx
        y += dy
        if x < 0 or x >= len(self.array[0]) or y < 0 or y >= len(self.array):
            return 0
        if self.array[y][x] == "#":
            return 0
        return self.score_map[(x, y)] - score - abs(dx) - abs(dy) >= 100

    def cheat(self):
        total_score_saved_count = 0
        for y in range(len(self.array)):
            for x in range(len(self.array[0])):
                if self.array[y][x] in [".", "S"]:
                    for dy in range(-20, 21):
                        for dx in range(abs(dy) - 20, 21 - abs(dy)):
                            total_score_saved_count += self.check(x, dx, y, dy, self.score_map[(x, y)])
        return total_score_saved_count

    def solve(self, s):
        self.parse_input(s)

        self.bfs()

        return self.cheat()


def solve(s):
    return Solution().solve(s)
