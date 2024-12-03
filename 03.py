from utils import timed, get_input_lines

import re

def mul(x, y):
    return x*y

def part_1(input_lines):
    memory = "".join(input_lines)
    pattern = re.compile('mul\(\d+\,\d+\)')
    calls = pattern.findall(memory)
    return sum(eval(call) for call in calls)  # lol


def part_2(input_lines):
    memory = "".join(input_lines)
    pattern =re.compile("mul\(\d+\,\d+\)|do\(\)|don't\(\)")
    calls = pattern.findall(memory)
    result = 0
    enabled = True
    for call in calls:
        if call == "do()":
            enabled = True
        elif call == "don't()":
            enabled = False
        elif enabled:
            result += eval(call)  # lol
    return result


timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])