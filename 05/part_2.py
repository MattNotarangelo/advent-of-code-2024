# https://adventofcode.com/2024/day/5

from collections import defaultdict


def parse_input(s):
    s = s.split("\n\n")
    input_1 = s[0].split("\n")
    input_2 = s[1].split("\n")
    return input_1, [i.split(",") for i in input_2]


def build_graph(s):
    dependencies = defaultdict(set)
    for i in s:
        split_line = i.split("|")
        dependencies[split_line[1]].add(split_line[0])

    return dependencies


def get_all_numbers(s):
    ret = set()
    for i in s:
        split_line = i.split("|")
        ret.add(split_line[0])
        ret.add(split_line[1])
    return ret


def remove_nums_in_row(s: set, nums):
    for i in nums:
        s.remove(i)
    return s


def reorder_rows(rows, s1, g):
    corrected_rows = []
    for copy in rows:
        row = copy.copy()
        for left in range(len(row)):
            for right in range(len(row)):
                if left != right:
                    if row[left] not in g[row[right]]:
                        tmp = row[left]
                        row[left] = row[right]
                        row[right] = tmp
        corrected_rows.append(row)

    return corrected_rows


def solve(s):
    s1, s2 = parse_input(s)

    g = build_graph(s1)

    invalid_rows = []

    for row in s2:

        seen = get_all_numbers(s1)
        remove_nums_in_row(seen, row)
        invalid = False
        for i in row:
            if not seen.issuperset(g[i]):
                invalid = True
            seen.add(i)
        if invalid:
            invalid_rows.append(row)

    count = 0
    for row in reorder_rows(invalid_rows, s1, g):
        count += int(row[len(row) // 2])

    return count
