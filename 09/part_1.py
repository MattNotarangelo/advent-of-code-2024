# https://adventofcode.com/2024/day/9


def parse_input(s):
    return [int(i) for i in list(s.strip())]


def solve(s):
    s = parse_input(s)
    stack = []
    res = []

    for i in range(len(s)):
        if i % 2 == 0:
            stack.extend([i // 2] * s[i])

    stack_size = len(stack)
    for i in range(len(s)):
        if i % 2 == 0:
            res.extend([i // 2] * s[i])
        else:
            for _ in range(s[i]):
                if stack:
                    res.append(stack.pop())

    res = res[:stack_size]
    return sum([i * res[i] for i in range(len(res))])
