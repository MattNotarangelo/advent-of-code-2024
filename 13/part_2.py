# https://adventofcode.com/2024/dy_a/13
import re

COST = {
    "A": 3,
    "B": 1,
}

INCR = 10000000000000


def parse_input(s):
    ret = []
    s = s.split("\n")
    for i in [s[j : j + 4] for j in range(0, len(s), 4)]:
        tmp = {}
        for k in i:
            m = re.findall(r"Button (A|B): X\+(\d+), Y\+(\d+)", k)
            if not m:
                m = re.findall(r"Prize: X=(\d+), Y=(\d+)", k)
            if len(m) > 0:
                if m[0][0] == "A" or m[0][0] == "B":
                    tmp[m[0][0]] = (int(m[0][1]), int(m[0][2]))
                if len(m[0]) == 2:
                    tmp["P"] = (int(m[0][0]), int(m[0][1]))
        ret.append(tmp)
    return ret


def solve(s):

    total_cost = 0
    s = parse_input(s)

    for i in s:
        x_a, y_a = i["A"]
        x_b, y_b = i["B"]
        p_x, p_y = i["P"]
        p_x += INCR
        p_y += INCR
        solution_a, solution_b = None, None

        if (x_b * p_y - y_b * p_x) / (x_b * y_a - y_b * x_a) == (x_b * p_y - y_b * p_x) // (x_b * y_a - y_b * x_a):
            solution_a = (x_b * p_y - y_b * p_x) // (x_b * y_a - y_b * x_a)
            if (p_y - solution_a * y_a) / y_b == (p_y - solution_a * y_a) // y_b:
                solution_b = (p_y - solution_a * y_a) // y_b
        if solution_a is not None and solution_b is not None:
            total_cost += COST["A"] * solution_a + COST["B"] * solution_b

    return int(total_cost)
