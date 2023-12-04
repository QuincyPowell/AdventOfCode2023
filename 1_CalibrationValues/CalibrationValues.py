import sys
import re

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
WORD_DIGITS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
WORD_DIGITS_REVERSE = ["orez", "eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin"]
TRANSLATION_DICT = {"zero": "0", "orez": "0",
                    "one": "1", "eno": "1",
                    "two": "2", "owt": "2",
                    "three": "3", "eerht": "3",
                    "four": "4", "ruof": "4",
                    "five": "5", "evif": "5",
                    "six": "6", "xis": "6",
                    "seven": "7", "neves": "7",
                    "eight": "8", "thgie": "8",
                    "nine": "9", "enin": "9"}

def get_calibration_line_value(line):
    first = "0"
    first_pos = len(line)
    last = "0"
    last_pos = len(line)
    # Find leftmost matching digit as numeral or word
    for digit in DIGITS:
        match = re.search(digit, line)
        if (match and match.span()[0] < first_pos):
            first_pos = match.span()[0]
            first = digit
    for digit in WORD_DIGITS:
        match = re.search(digit, line)
        if (match and match.span()[0] < first_pos):
            first_pos = match.span()[0]
            first = TRANSLATION_DICT[digit]
    # Find rightmost matching digit as numeral or word
    line_reversed = line[::-1]
    for digit in DIGITS:
        match = re.search(digit, line_reversed)
        if (match and match.span()[0] < last_pos):
            last_pos = match.span()[0]
            last = digit
    for digit in WORD_DIGITS_REVERSE:
        match = re.search(digit, line_reversed)
        if (match and match.span()[0] < last_pos):
            last_pos = match.span()[0]
            last = TRANSLATION_DICT[digit]
    # result
    print("Line: " + line + "Interpreted as: " + first + last)
    return int(first + last)

calibration_value_sum = 0

print("Trying to open: " + sys.argv[1])
with open(sys.argv[1], "r", encoding="utf-8") as file:
    for line in file:
        calibration_value_sum += get_calibration_line_value(line)

print("Calculated sum of calibration values: " + str(calibration_value_sum))
