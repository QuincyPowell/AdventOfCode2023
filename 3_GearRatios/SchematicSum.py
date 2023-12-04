import sys
import re

NOT_PART = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "\n"]

part_num_sum = 0

def scan_schematic_line(prev, curr, next):
    line_parts_sum = 0
    matchnumsre = re.compile("[0-9]+")
    # scan current line any numbers
    fitr = re.finditer(matchnumsre, curr)
    for m in fitr:
        part_num = int(m.group())
        back = m.span()[0] - 1
        front = m.span()[1]
        print("checking part number " + str(part_num) + " for adjacent part symbol in range (" + str(back) + ", " + str(front) + ")")
        # check adjacent elements for part symbol, eager approach
        if (back >= 0  and curr[back] not in NOT_PART):
            print("part found: " + str(part_num) + " on current line at " + str(back) + " part sym: " + curr[back])
            line_parts_sum += part_num
            continue
        if (front < len(curr) and curr[front] not in NOT_PART):
            print("part found: " + str(part_num) + " on current line at " + str(front) + " part sym: " + curr[front])
            line_parts_sum += part_num
            continue
        if back < 0:
            back = 0
        if front >= len(curr):
            front = len(curr) - 1
        found_part = False
        if (front < len(prev)):
            cursor = back
            while (cursor <= front):
                if (prev[cursor] not in NOT_PART):
                    found_part = True
                    print("part found: " + str(part_num) + " on previous line at " + str(cursor) + " part sym: " + prev[cursor])
                    break
                cursor += 1
        if (not found_part and front < len(next)):
            cursor = back
            while (cursor <= front):
                if (next[cursor] not in NOT_PART):
                    found_part = True
                    print("part found: " + str(part_num) + " on next line at " + str(cursor) + " part sym: " + next[cursor])
                    break
                cursor += 1
        if found_part:
            line_parts_sum += part_num

    return line_parts_sum

with open(sys.argv[1], "r", encoding="utf-8") as file:
    prev_line = ""
    curr_line = file.readline()
    next_line = file.readline()
    part_num_sum += scan_schematic_line(prev_line, curr_line, next_line)
    for line in file:
        prev_line = curr_line
        curr_line = next_line
        next_line = line
        part_num_sum += scan_schematic_line(prev_line, curr_line, next_line)
    prev_line = curr_line
    curr_line = next_line
    next_line = ""
    part_num_sum += scan_schematic_line(prev_line, curr_line, next_line)

print("Final sum of part numbers: " + str(part_num_sum))