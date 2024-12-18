# https://adventofcode.com/2024/day/18
import collections

inf = float("inf")
SIZE = (71, 71)


class Solution:
    def __init__(self):
        self.bytes = []
        self.array = [["."] * SIZE[0] for _ in range(SIZE[1])]
        self.shortest_path = inf
        self.bytes_fallen = 1024

    def parse_input(self, s):
        s = s.split("\n")
        for i in s:
            self.bytes.append((int(i.split(",")[0]), int(i.split(",")[1])))

    def bfs(self):
        # stack contains tuple of (x_pos, y_pos, score, path)
        stack: collections.deque[tuple[int, int, int, list]] = collections.deque()
        stack.append((0, 0, 0, []))
        seen = set()

        while len(stack) > 0:
            x, y, score, path = stack.popleft()
            if x < 0 or x >= SIZE[0] or y < 0 or y >= SIZE[1]:
                continue
            if self.array[y][x] == "#":
                continue
            if (x, y) in seen:
                continue
            if score > self.shortest_path:
                continue

            if (x, y) == (SIZE[0] - 1, SIZE[1] - 1):
                self.shortest_path = min(self.shortest_path, score)
                continue

            seen.add((x, y))
            stack.append((x + 1, y, score + 1, path + [(x, y)]))
            stack.append((x - 1, y, score + 1, path + [(x, y)]))
            stack.append((x, y + 1, score + 1, path + [(x, y)]))
            stack.append((x, y - 1, score + 1, path + [(x, y)]))
        return

    def add_to_array(self, pos):
        self.array[pos[1]][pos[0]] = "#"

    def solve(self, s):
        self.parse_input(s)
        for i in self.bytes[: self.bytes_fallen]:
            self.add_to_array(i)

        self.bfs()

        return self.shortest_path

    def print_array(self):
        copy = [i[:] for i in self.array]
        for i in copy:
            print("".join(i))


def solve(s):
    return Solution().solve(s)
