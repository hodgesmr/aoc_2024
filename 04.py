from utils import timed, get_input_lines


def part_1(input_lines):
    count = 0
    # count forward every row
    count += sum([row.count("XMAS") for row in input_lines])

    # count backward every row
    count += sum([row[::-1].count("XMAS") for row in input_lines])

    # count forward every column
    cols = [
        "".join([row[i] for row in input_lines]) for i in range(len(input_lines[0]))
    ]
    count += sum([col.count("XMAS") for col in cols])

    # count backward every column
    count += sum([col[::-1].count("XMAS") for col in cols])

    # onto the diags...
    diags = []

    # forward
    # top-right, rightward diags
    for x, _ in enumerate(input_lines[0]):
        xi = x
        y = 0
        diag = ""
        while y < len(input_lines) and xi < len(input_lines[0]):
            c = input_lines[y][xi]
            diag += c
            y += 1
            xi += 1
        diags.append(diag)

    # bottom-left, rightward diags
    y = 1
    while y < len(input_lines):
        yi = y
        xi = 0
        diag = ""
        while yi < len(input_lines) and xi < len(input_lines[y]):
            c = input_lines[yi][xi]
            diag += c
            yi += 1
            xi += 1
        diags.append(diag)
        y += 1

    # backward

    # top-right, leftward diags
    for x, _ in enumerate(reversed(input_lines[0])):
        xi = x
        y = 0
        diag = ""
        while y < len(input_lines) and xi < len(input_lines[0]):
            c = list(reversed(input_lines[y]))[xi]
            diag += c
            y += 1
            xi += 1
        diags.append(diag)

    # bottom-left, leftward diags
    y = 1
    while y < len(input_lines):
        yi = y
        xi = 0
        diag = ""
        while yi < len(input_lines) and xi < len(input_lines[y]):
            c = list(reversed(input_lines[yi]))[xi]
            diag += c
            yi += 1
            xi += 1
        diags.append(diag)
        y += 1

    # count forward every diagonal
    count += sum([diag.count("XMAS") for diag in diags])

    # count backward every diagonal
    count += sum([diag[::-1].count("XMAS") for diag in diags])

    return count


def part_2(input_lines):
    count = 0

    # just loop through the whole thing once
    # but skipe the outer 1 elements
    # and then look in the diagonald directions
    # and count the SAM / MAS whenever we see A

    x = 1
    y = 1
    while y < len(input_lines)-1:
        while x < len(input_lines[y])-1:
            letter = input_lines[x][y]
            if letter == "A":
                cross = input_lines[x-1][y-1] + "A" + input_lines[x+1][y+1]
                if cross == "SAM" or cross == "MAS":
                    cross = input_lines[x-1][y+1] + "A" + input_lines[x+1][y-1]
                    if cross == "SAM" or cross == "MAS":
                        count += 1
            x += 1
        x = 1
        y += 1
    return count



timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
