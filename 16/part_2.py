# https://adventofcode.com/2024/day/16
import sys
import collections

print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)

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
        self.seen = collections.defaultdict(dict)
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

    def dfs(self, position, direction, score, path_orig, start=False):
        path = path_orig[:]
        if not start:
            position = move(position, direction)
            path.append(tuple(position))
        if self.array[position[1]][position[0]] == "#":
            return
        if position == self.end:
            self.min_score = min(self.min_score, score)
            self.paths[score].append(path)
            return

        if score > self.min_score:  # give up
            return

        tupled_pos = tuple(position)
        if tupled_pos in self.seen and direction in self.seen[tupled_pos] and self.seen[tupled_pos][direction] < score:
            return

        self.seen[tupled_pos][direction] = score

        self.dfs(
            position,
            direction,
            score + 1,
            path,
        )
        self.dfs(
            position,
            MAP[direction]["L"],
            score + 1001,
            path,
        )  # rotate and move
        self.dfs(
            position,
            MAP[direction]["R"],
            score + 1001,
            path,
        )  # rotate and move
        # self.dfs(
        #     move(position, MAP[MAP[direction]["R"]]["R"]),
        #     MAP[MAP[direction]["R"]]["R"],
        #     score + 2001,
        #     path[:] + [move(position, MAP[MAP[direction]["R"]]["R"])],
        # )  # rotate and move

    def solve(self, s):
        self.parse_input(s)

        self.dfs(self.start, self.direction, 0, [], start=True)
        min_tiles = set()
        for path in self.paths[self.min_score]:
            for i in path:
                min_tiles.add(tuple(i))
        return len(min_tiles) + 1

    def print_array(self, path):
        copy = [i[:] for i in self.array]
        # for path in self.paths[self.min_score]:
        for i in path:
            copy[i[1]][i[0]] = "X"
        for i in copy:
            print("".join(i))


def solve(s):
    return Solution().solve(s)
