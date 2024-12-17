# https://adventofcode.com/2024/day/

MAPPING = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}


def upgrade_to_part_2(s):
    return s.replace("#", "##").replace(".", "..").replace("O", "[]").replace("@", "@.")


class Solution:
    def __init__(self):
        self.array = []
        self.actions = ""
        self.position = [-1, -1]

    def print_array(self):
        for i in self.array:
            print("".join(i))

    def parse_input(self, s):
        s = s.split("\n\n")
        self.array = [list(i) for i in upgrade_to_part_2(s[0]).split("\n")]
        self.actions = s[1].replace("\n", "")
        for y in range(len(self.array)):
            for x in range(len(self.array[0])):
                if self.array[y][x] == "@":
                    self.position = [x, y]
                    return

    def move(self, direction):
        cur = self.position[:]
        if self.array[cur[1] + direction[1]][cur[0] + direction[0]] == "#":
            pass
        elif self.array[cur[1] + direction[1]][cur[0] + direction[0]] == ".":
            self.array[cur[1]][cur[0]] = "."
            cur[0] += direction[0]
            cur[1] += direction[1]
            self.array[cur[1]][cur[0]] = "@"
            self.position = cur
        else:
            while True:
                cur[0] += direction[0]
                cur[1] += direction[1]
                if self.array[cur[1]][cur[0]] == "#":
                    return
                elif self.array[cur[1]][cur[0]] == ".":
                    # self.array[cur[1]][cur[0]] = "O"
                    # self.array[self.position[1]][self.position[0]] = "."
                    # self.position[0] += direction[0]
                    # self.position[1] += direction[1]
                    # self.array[self.position[1]][self.position[0]] = "@"
                    # return

    def calculate_score(self):
        score = 0
        for y in range(len(self.array)):
            for x in range(len(self.array[0])):
                if self.array[y][x] == "[":
                    score += y * 100 + x
        return score

    def solve(self, s):
        self.parse_input(s)
        self.print_array()
        # for i in self.actions:
        #     self.move(MAPPING[i])

        # return self.calculate_score()


def solve(s):
    return Solution().solve(s)
