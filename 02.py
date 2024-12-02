from utils import timed, get_input_lines


def is_safe(report):
    operator = (lambda x, y: x < y) if report[0] < report[1] else (lambda x, y: x > y)
    safe = True
    i = 0
    while safe and i < len(report) - 1:
        value1 = report[i]
        value2 = report[i + 1]
        safe = (
            operator(value1, value2)
            and abs(value1 - value2) >= 1
            and abs(value1 - value2) <= 3
        )
        i += 1
    return safe


# Check each report to see if it's safe
def part_1(input_lines):
    return sum(
        [
            is_safe(report)
            for report in [
                [int(level) for level in report.split()] for report in input_lines
            ]
        ]
    )

# Check each possible slice of each report, and see if any are safe
# By definition, if a full report is safe, so is a slice
def part_2(input_lines):
    return sum(
        [
            any([is_safe(report[:i] + report[i + 1 :]) for i in range(len(report))])
            for report in [
                [int(level) for level in report.split()] for report in input_lines
            ]
        ]
    )


timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
