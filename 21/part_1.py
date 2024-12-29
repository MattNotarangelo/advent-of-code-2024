# https://adventofcode.com/2024/day/21

DOOR_MAP = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"],
]

ROBOT_MAP = [
    [None, "^", "A"],
    ["<", "v", ">"],
]


def get_index(char, mapping):
    for y in range(len(mapping)):
        for x in range(len(mapping[0])):
            if mapping[y][x] == char:
                return x, y
    raise Exception("Invalid robot char", char)


def move_keypad(curr, target, mapping):
    ret = ""
    curr_x, curr_y = get_index(curr, mapping)
    target_x, target_y = get_index(target, mapping)

    diff_x = target_x - curr_x
    diff_y = target_y - curr_y

    if diff_y < 0:
        ret += "^" * abs(diff_y)
    elif diff_y > 0:
        ret += "v" * abs(diff_y)

    if diff_x < 0:
        ret += "<" * abs(diff_x)
    elif diff_x > 0:
        ret += ">" * abs(diff_x)

    return ret + "A"


def move_keypad_door(curr, target):
    return move_keypad(curr, target, DOOR_MAP)


def move_keypad_robot(curr, target):
    return move_keypad(curr, target, ROBOT_MAP)


def parse_input(s):
    return [list(i) for i in s.split("\n")]


def calculate(door_input):
    first_keypad = ""
    second_keypad = ""
    third_keypad = ""
    print("FIRST")
    curr = "A"
    for i in door_input:
        first_keypad += move_keypad_door(curr, i)
        curr = i

    print("SECOND")
    curr = "A"
    for i in first_keypad:
        second_keypad += move_keypad_robot(curr, i)
        curr = i

    print("THIRD")
    curr = "A"
    for i in second_keypad:
        third_keypad += move_keypad_robot(curr, i)
        curr = i

    return int("".join(door_input[:-1])) * len(third_keypad)


def solve(s):
    total_score = 0
    s = parse_input(s)
    for i in s:
        total_score += calculate(i)
    return total_score
