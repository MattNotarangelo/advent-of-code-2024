# https://adventofcode.com/2024/day/13
import re

COST = {
    "A": 3,
    "B": 1,
}


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
        change_x_a, change_y_a = i["A"]
        change_x_b, change_y_b = i["B"]
        target_x, target_y = i["P"]
        for a_presses in range(100):
            target_x_remaining = target_x - change_x_a * a_presses
            target_y_remaining = target_y - change_y_a * a_presses

            if target_x_remaining < 0 or target_y_remaining < 0:
                break

            if target_x_remaining == 0 and target_y_remaining == 0:
                total_cost += a_presses * COST["A"]

            b_presses_required = target_x_remaining / change_x_b

            if b_presses_required == int(b_presses_required) and target_y_remaining / change_y_b == int(b_presses_required):
                total_cost += a_presses * COST["A"] + b_presses_required * COST["B"]

    return int(total_cost)
