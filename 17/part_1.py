# https://adventofcode.com/2024/day/17


class Solution:
    def __init__(self) -> None:
        self.reg_a = 0
        self.reg_b = 0
        self.reg_c = 0
        self.ptr = 0
        self.program = []

    def parse_input(self, s):
        s = s.split("\n")
        self.reg_a = int(s[0][11:])
        self.reg_b = int(s[1][11:])
        self.reg_c = int(s[2][11:])
        self.program = [int(i) for i in s[4][9:].split(",")]

    def parse_operand(self, opcode, operand):

        if opcode in [1, 3]:
            return operand

        if operand in [0, 1, 2, 3]:
            return operand
        if operand == 4:
            return self.reg_a
        if operand == 5:
            return self.reg_b
        if operand == 6:
            return self.reg_c
        raise ValueError(f"Invalid operand: {operand}")

    def process_command(self, opcode, arg):
        # print(f"opcode: {opcode}, arg: {arg}")
        if opcode == 0:
            self.reg_a = int(self.reg_a / (2**arg))
        elif opcode == 1:
            self.reg_b = self.reg_b ^ arg
        elif opcode == 2:
            self.reg_b = arg % 8
        elif opcode == 3:
            if self.reg_a == 0:
                return 0
            self.ptr = arg - 2  # subtract 2 because it gets added later anyway
        elif opcode == 4:
            self.reg_b = self.reg_b ^ self.reg_c
        elif opcode == 5:
            return arg % 8
        elif opcode == 6:
            self.reg_b = int(self.reg_a / (2**arg))
        elif opcode == 7:
            self.reg_c = int(self.reg_a / (2**arg))
        else:
            raise ValueError(f"Invalid opcode: {opcode}")

    def solve(self, s):
        result = []

        self.parse_input(s)

        while self.ptr >= 0 and self.ptr < len(self.program) - 1:
            opcode = self.program[self.ptr]
            operand = self.program[self.ptr + 1]

            result += [self.process_command(opcode, self.parse_operand(opcode, operand))]

            self.ptr += 2
        return ",".join([str(i) for i in result[:-1] if i != None])


def solve(s):
    return Solution().solve(s)
