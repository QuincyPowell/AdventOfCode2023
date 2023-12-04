import sys
import re

GEAR = "*"

current_line_num = 0
potential_gears = {}

def scan_line_for_gears(prev, curr, next):
    matchnumsre = re.compile("[0-9]+")
    # scan current line for numbers
    fitr = re.finditer(matchnumsre, curr)
    for m in fitr:
        part_num = int(m.group())
        back = m.span()[0] - 1
        front = m.span()[1]
        print("checking part number " + str(part_num) + " for adjacent gear symbol in range (" + str(back) + ", " + str(front) + ")")
        # check adjacent elements for part symbol, check all (thorough approach)
        if (back >= 0 and curr[back] is GEAR):
            position = (back, current_line_num)
            print("possible gear found: " + str(part_num) + " on current line at " + str(position) + " part sym: " + curr[back])
            if position in potential_gears:
                potential_gears[position].append(part_num)
            else:
                potential_gears[position] = [part_num]
        if (front < len(curr) and curr[front] is GEAR):
            position = (front, current_line_num)
            print("possible gear found: " + str(part_num) + " on current line at " + str(position) + " part sym: " + curr[front])
            if position in potential_gears:
                potential_gears[position].append(part_num)
            else:
                potential_gears[position] = [part_num]
        if back < 0:
            back = 0
        if front >= len(curr):
            front = len(curr) - 1
        if front < len(prev):
            cursor = back
            while cursor <= front:
                if prev[cursor] is GEAR:
                    position = (cursor, current_line_num - 1)
                    print("possible gear found: " + str(part_num) + " on previous line at " + str(position) + " part sym: " + prev[cursor])
                    if position in potential_gears:
                        potential_gears[position].append(part_num)
                    else:
                        potential_gears[position] = [part_num]
                cursor += 1
        if front < len(next):
            cursor = back
            while cursor <= front:
                if next[cursor] is GEAR:
                    position = (cursor, current_line_num + 1)
                    print("possible gear found: " + str(part_num) + " on next line at " + str(position) + " part sym: " + next[cursor])
                    if position in potential_gears:
                        potential_gears[position].append(part_num)
                    else:
                        potential_gears[position] = [part_num]
                cursor += 1

with open(sys.argv[1], "r", encoding="utf-8") as file:
    prev_line = ""
    curr_line = file.readline()
    next_line = file.readline()
    scan_line_for_gears(prev_line, curr_line, next_line)
    for line in file:
        current_line_num += 1
        prev_line = curr_line
        curr_line = next_line
        next_line = line
        scan_line_for_gears(prev_line, curr_line, next_line)
    current_line_num += 1
    prev_line = curr_line
    curr_line = next_line
    next_line = ""
    scan_line_for_gears(prev_line, curr_line, next_line)

# find gears out of potential gears and calculate gear ratio
gear_ratio_sum = 0
for key, value in potential_gears.items():
    print("checking possible gear at " + str(key) + " which has part count " + str(len(value)))
    if len(value) == 2:
        gear_ratio = value[0] * value[1]
        print("actual gear found at: " + str(key) + " with gear ratio " + str(gear_ratio))
        gear_ratio_sum += gear_ratio

print("Total gear ratio: " + str(gear_ratio_sum))