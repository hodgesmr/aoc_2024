from utils import timed, get_input_lines

from collections import defaultdict


def part_1(input_lines):
    page_map = defaultdict(set)
    total = 0

    for line in input_lines:
        # build the page map: int:set(int)
        if "|" in line:
            page1, page2 = [int(page) for page in line.split("|")]
            page_map[page1].add(page2)

        # walk the updates
        elif line:
            update_steps = [int(page) for page in line.split(",")]
            invalid = False
            valid_next = page_map[update_steps[0]]
            i = 1
            while i < len(update_steps) and not invalid:
                step = update_steps[i]
                if step not in valid_next:
                    invalid = True
                else:
                    valid_next = page_map[step]
                i += 1
            # add the middle item if it's valid
            if not invalid:
                middle_item = update_steps[len(update_steps) // 2]
                total += middle_item

    return total



def part_2(input_lines):
    page_map = defaultdict(set)
    total = 0

    for line in input_lines:
        # build the page map: int:set(int)
        if "|" in line:
            page1, page2 = [int(page) for page in line.split("|")]
            page_map[page1].add(page2)

        # walk the updates
        elif line:
            update_steps = [int(page) for page in line.split(",")]
            invalid = False
            valid_next = page_map[update_steps[0]]
            i = 1
            while i < len(update_steps) and not invalid:
                step = update_steps[i]
                if step not in valid_next:
                    # we're in an invalid update; let's correct it here
                    invalid = True
                    corrected_steps = []
                    while update_steps:
                        # list all the valid next steps 
                        valid_next_steps = [page_map[x] for x in update_steps]
                        # find the item that doesn't appear in any next steps, that's our "first"
                        item = [x for x in update_steps if all(x not in s for s in valid_next_steps)]
                        # push it onto the corrected steps
                        corrected_steps.append(item[0])
                        # remove, repeat
                        update_steps.remove(item[0])

                    middle_item = corrected_steps[len(corrected_steps) // 2]
                    total += middle_item

                else:
                    valid_next = page_map[step]
                i += 1
            
    return total


timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
