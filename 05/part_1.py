# https://adventofcode.com/2024/day/5

"""
Had some confusion with this one

If 5|6 and 6|7, then 5|7. But it seems like the input must have 5|7 (whether intentionally or not, eg. no intermediate steps)

For part 1 I created a dependency graph and used that to check if there were nodes between the numbers in the row (eg. 1|2, 2|3. Input = 1,3 is valid)

For part 2 I had to reorder the rows to make sure that the numbers were in the correct order. I did this by swapping numbers in the row until they were in the correct order. This uses the assumptions that there is always a x|y for every number in the input (eg. x,y,z always has x|y and y|z)

"""

from collections import defaultdict


def parse_input(s):
    s = s.split("\n\n")
    input_1 = s[0].split("\n")
    input_2 = s[1].split("\n")
    return input_1, input_2


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
    for i in nums.split(","):
        s.remove(i)
    return s


def solve(s):
    s1, s2 = parse_input(s)

    g = build_graph(s1)

    valid_rows = []

    for row in s2:

        seen = get_all_numbers(s1)
        remove_nums_in_row(seen, row)
        invalid = False
        for i in row.split(","):
            if not seen.issuperset(g[i]):
                invalid = True
            seen.add(i)
        if invalid:
            continue
        valid_rows.append(row)

    count = 0
    for row in valid_rows:
        split_row = row.split(",")
        count += int(split_row[len(split_row) // 2])

    return count
