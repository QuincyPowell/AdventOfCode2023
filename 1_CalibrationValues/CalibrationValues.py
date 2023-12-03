import sys

def get_calibration_line_value(line):
    first = "0"
    last = "0"
    cursor = 0
    line_len = len(line)
    # scan forward
    while (cursor < line_len):
        if line[cursor] in DIGITS:
            first = line[cursor]
            break
        cursor += 1
    # scan backward
    cursor = line_len - 1
    while (cursor >= 0):
        if line[cursor] in DIGITS:
            last = line[cursor]
            break
        cursor -= 1
    # result
    print("Line: " + line + "Interpreted as: " + first + last)
    return int(first + last)

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

calibration_value_sum = 0

print("Trying to open: " + sys.argv[1])
with open(sys.argv[1], "r", encoding="utf-8") as file:
    for line in file:
        if (line == ""):
            break
        calibration_value_sum += get_calibration_line_value(line)

print("Calculated sum of calibration values: " + str(calibration_value_sum))
