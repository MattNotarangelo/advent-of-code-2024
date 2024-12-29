# https://adventofcode.com/2024/day/9


def parse_input(s):
    return [int(i) for i in list(s.strip())]


def repr(s) -> str:
    ret = ""
    for i in s:
        ret += i["quantity"] * str(i["item"])
    return ret


def calculate_score(s):
    score = 0
    for i in range(len(s)):
        if s[i] != ".":
            score += i * int(s[i])
    return score


def solve(s):
    s = parse_input(s)
    stack = []
    for i in range(len(s)):
        if i % 2 == 0:
            stack.append({"item": i // 2, "quantity": s[i]})
        if i % 2 == 1:
            stack.append({"item": ".", "quantity": s[i]})
    ret = stack.copy()

    for i in stack[::-1]:
        pos = 0
        for l in stack:
            if l == i:
                break
            pos += l["quantity"]
        to_check_name = i["item"]
        if to_check_name == ".":
            continue
        to_check_quantity = i["quantity"]
        for j in range(len(ret)):
            if ret[j]["item"] == "." and ret[j]["quantity"] >= to_check_quantity and j < pos:
                for k in range(len(ret)):
                    if ret[k] == i:
                        ret[k]["item"] = "."

                ret[j]["quantity"] -= to_check_quantity
                ret.insert(j, {"item": to_check_name, "quantity": to_check_quantity})
                break

    return calculate_score(repr(ret))
