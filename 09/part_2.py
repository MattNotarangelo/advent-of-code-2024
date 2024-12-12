# https://adventofcode.com/2024/day/9


def parse_input(s):
    return [int(i) for i in list(s.strip())]


def solve(s):
    return 0
    s = parse_input(s)
    print(s)
    file_stack = []
    free_stack = []
    res = []

    for i in range(len(s)):
        if i % 2 == 0:
            file_stack.append([i // 2] * s[i])
        if i % 2 == 1:
            free_stack.append(["."] * s[i])

    stack_size = len(file_stack)
    for i in range(len(s)):
        if i % 2 == 0:
            res.extend([i // 2] * s[i])
        else:
            for _ in range(s[i]):
                if file_stack:
                    res.append(file_stack.pop())

    res = res[:stack_size]
    return sum([i * res[i] for i in range(len(res))])
