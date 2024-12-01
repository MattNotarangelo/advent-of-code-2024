from collections import Counter


def parse_input(s: str) -> tuple[list[int], list[int]]:
    c1 = []
    c2 = []
    for i in s.strip().split("\n"):
        items = i.split("   ")
        c1.append(int(items[0]))
        c2.append(int(items[1]))

    return c1, c2


def part1(s: str) -> int:
    score = 0

    c1, c2 = parse_input(s)
    c1.sort()
    c2.sort()

    for i, j in zip(c1, c2):
        score += abs(i - j)

    return score


def part2(s: str) -> int:
    score = 0

    c1, c2 = parse_input(s)
    counter_c2 = Counter(c2)

    for i in c1:
        score += counter_c2[i] * i

    return score


if __name__ == "__main__":
    with open("input.txt") as f:
        INPUT = f.read()
    print(f"{part1(INPUT) = }")
    print(f"{part2(INPUT) = }")
