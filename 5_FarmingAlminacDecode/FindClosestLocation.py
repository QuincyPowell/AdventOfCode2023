import sys

seeds = []
seed_soil_map = {}
soil_fert_map = {}
fert_watr_map = {}
watr_lght_map = {}
lght_temp_map = {}
temp_hmid_map = {}
hmid_lctn_map = {}

def get_seeds(seed_line):
    seeds_str = seed_line.split(": ")[1]
    for seed in seeds_str.split():
        seeds.append(int(seed))

def process_line_into_map(line, map):
    #print("Attempting to add this line to a map: " + line)
    split = line.split()
    range_start = int(split[1])
    range_end = range_start + int(split[2])
    offset = range_start - int(split[0])
    key_range = range(range_start, range_end)
    map[key_range] = offset

def decode_by_map(input, map):
    for key, value in map.items():
        #print(str(key) + str(value) + " " + str(input))
        if input in key:
            print(str(input) + " in range " + str(key))
            return input - value
    #print("mapped " + str(input) + " to " + str(input))
    return input

with open(sys.argv[1], "r", encoding="utf-8") as file:
    # seed line is always first
    get_seeds(file.readline())
    #  seed to soil map always starts on line 3
    file.readline()
    map_id = file.readline()
    if map_id.strip() != "seed-to-soil map:":
        print("Unexpected input format at seed->soil. Expect the unexpected.")
    line = file.readline()
    while line != "\n":
        process_line_into_map(line, seed_soil_map)
        line = file.readline()
    # seed to fertilizer map
    map_id = file.readline()
    if map_id.strip() != "soil-to-fertilizer map:":
        print("Unexpected input format at soil->fertilizer. Expect the unexpected.")
    line = file.readline()
    while line != "\n":
        process_line_into_map(line, soil_fert_map)
        line = file.readline()
    # fertilizer to water map
    map_id = file.readline()
    if map_id.strip() != "fertilizer-to-water map:":
        print("Unexpected input format at fertilzer->water. Expect the unexpected.")
    line = file.readline()
    while line != "\n":
        process_line_into_map(line, fert_watr_map)
        line = file.readline()
    # water to light map
    map_id = file.readline()
    if map_id.strip() != "water-to-light map:":
        print("Unexpected input format at water->light. Expect the unexpected.")
    line = file.readline()
    while line != "\n":
        process_line_into_map(line, watr_lght_map)
        line = file.readline()
    # light to temperature map
    map_id = file.readline()
    if map_id.strip() != "light-to-temperature map:":
        print("Unexpected input format at light->temperature. Expect the unexpected.")
    line = file.readline()
    while line != "\n":
        process_line_into_map(line, lght_temp_map)
        line = file.readline()
    # temperature to humidity map
    map_id = file.readline()
    if map_id.strip() != "temperature-to-humidity map:":
        print("Unexpected input format at temperature->humidity. Expect the unexpected.")
    line = file.readline()
    while line != "\n":
        process_line_into_map(line, temp_hmid_map)
        line = file.readline()
    # humidity to location map
    map_id = file.readline()
    if map_id.strip() != "humidity-to-location map:":
        print("Unexpected input format at humidity->location. Expect the unexpected.")
    line = file.readline()
    while line != "":
        process_line_into_map(line, hmid_lctn_map)
        line = file.readline()

locations = []
for seed in seeds:
    soil = decode_by_map(seed, seed_soil_map)
    fert = decode_by_map(soil, soil_fert_map)
    watr = decode_by_map(fert, fert_watr_map)
    lght = decode_by_map(watr, watr_lght_map)
    temp = decode_by_map(lght, lght_temp_map)
    hmid = decode_by_map(temp, temp_hmid_map)
    location = decode_by_map(hmid, hmid_lctn_map)
    print("seed " + str(seed) + " location " + str(location))
    locations.append(location)

print("Closest (min) location: " + str(min(locations)))