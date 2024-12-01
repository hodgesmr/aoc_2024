from collections import Counter
from utils import timed, get_input_lines

def get_lists(input_lines):
    list1 = []
    list2 = []
    for line in input_lines:
        item1, item2 = line.split()
        list1.append(int(item1))
        list2.append(int(item2))
    
    return list1, list2


def part_1(input_lines):
    return sum(
        map(lambda x, y: abs(x - y),
            *[sorted(i) for i in get_lists(input_lines)]
        )
    )

def part_2(input_lines):
    list1, list2 = get_lists(input_lines)
    c = Counter(list2)
    score = 0
    for item in list1:
        score += item*c[item]
    return score

timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])