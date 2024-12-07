#!/usr/bin/env python3

from typing import Callable


def runner(name: str, f: Callable, path: str):

    sample_input = open(f"{path}/sample_input.txt").read().strip()
    sample_output_part = open(f"{path}/sample_output_part_{name}.txt").read().strip()
    question_input = open(f"{path}/question_input.txt").read().strip()

    res = str(f(sample_input)) == sample_output_part
    if res:
        print(f"part {name} sample passed")
    else:
        print(f"part {name} sample FAILED")
        print(f"> expected output: {sample_output_part}")
        print(f"> actual output: {f(sample_input)}")

    # sample must pass for question to run
    if res:
        print(f"part {name} question output: {f(question_input)}")
