import sys

seeds = []
seed_soil_rules = []
soil_fert_rules = []
fert_watr_rules = []
watr_lght_rules = []
lght_temp_rules = []
temp_hmid_rules = []
hmid_lctn_rules = []

def get_seeds(seed_line):
    seeds_str = seed_line.split(": ")[1]
    seeds_array = seeds_str.split()
    last = len(seeds_array)
    i = 0
    while i < last:
        range_start = int(seeds_array[i])
        i += 1
        range_end = range_start + int(seeds_array[i])
        lseed_range = range(range_start, range_end)
        seeds.append(lseed_range)
        i += 1

def add_rule_to_rule_list(line, rule_list):
    split = line.split()
    next_start = int(split[0])
    curr_start = int(split[1])
    range_size = int(split[2])
    rule_tuple = (next_start, curr_start, range_size)
    i = 0
    for rule in rule_list:
        if rule[0] > next_start:
            break
    rule_list.insert(i, rule_tuple)

def binary_search_rules(num, rule_list):
    front = 0
    back = len(rule_list) - 1
    mid = 0
    while front <= back:
        mid = int((front + back) / 2)
        curr_rule = rule_list[mid]
        rule_range = range(curr_rule[0], curr_rule[0] + curr_rule[2])
        if num in rule_range:
            return curr_rule
        elif num < curr_rule[0]:
            back = mid - 1
        else:
            front = mid + 1
    return (num, num, 1) # default rule input == output

def reverse_map(num, rule_list):
    applicable_rule = binary_search_rules(num, rule_list)
    return num + (applicable_rule[1] - applicable_rule[0])

def reverse_lookup_location_to_seed(location):
    hmid = reverse_map(location, hmid_lctn_rules)
    temp = reverse_map(hmid, temp_hmid_rules)
    lght = reverse_map(temp,lght_temp_rules)
    watr = reverse_map(lght, watr_lght_rules)
    fert = reverse_map(watr, fert_watr_rules)
    soil = reverse_map(fert, soil_fert_rules)
    seed = reverse_map(soil, seed_soil_rules)
    return seed

def check_seed_in_seeds(seed):
    for seed_range in seeds:
        if seed in seed_range:
            return True
    return False

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
        add_rule_to_rule_list(line, seed_soil_rules)
        line = file.readline()
    seed_soil_rules.sort()
    # seed to fertilizer map
    map_id = file.readline()
    if map_id.strip() != "soil-to-fertilizer map:":
        print("Unexpected input format at soil->fertilizer. Expect the unexpected.")
    line = file.readline()
    while line != "\n":
        add_rule_to_rule_list(line, soil_fert_rules)
        line = file.readline()
    soil_fert_rules.sort()
    # fertilizer to water map
    map_id = file.readline()
    if map_id.strip() != "fertilizer-to-water map:":
        print("Unexpected input format at fertilzer->water. Expect the unexpected.")
    line = file.readline()
    while line != "\n":
        add_rule_to_rule_list(line, fert_watr_rules)
        line = file.readline()
    fert_watr_rules.sort()
    # water to light map
    map_id = file.readline()
    if map_id.strip() != "water-to-light map:":
        print("Unexpected input format at water->light. Expect the unexpected.")
    line = file.readline()
    while line != "\n":
        add_rule_to_rule_list(line, watr_lght_rules)
        line = file.readline()
    watr_lght_rules.sort()
    # light to temperature map
    map_id = file.readline()
    if map_id.strip() != "light-to-temperature map:":
        print("Unexpected input format at light->temperature. Expect the unexpected.")
    line = file.readline()
    while line != "\n":
        add_rule_to_rule_list(line, lght_temp_rules)
        line = file.readline()
    lght_temp_rules.sort()
    # temperature to humidity map
    map_id = file.readline()
    if map_id.strip() != "temperature-to-humidity map:":
        print("Unexpected input format at temperature->humidity. Expect the unexpected.")
    line = file.readline()
    while line != "\n":
        add_rule_to_rule_list(line, temp_hmid_rules)
        line = file.readline()
    temp_hmid_rules.sort()
    # humidity to location map
    map_id = file.readline()
    if map_id.strip() != "humidity-to-location map:":
        print("Unexpected input format at humidity->location. Expect the unexpected.")
    line = file.readline()
    while line != "":
        add_rule_to_rule_list(line, hmid_lctn_rules)
        line = file.readline()
    hmid_lctn_rules.sort()

# find the lowest location that reverse maps to a seed
location = 0
max_location = 30000000000 # Some rule values go as high as about this, so it's an OK stop for an exercise
test_seed = None
while location < max_location:
    test_seed = reverse_lookup_location_to_seed(location)
    #print("location " + str(location) + " reverse mapped to seed " + str(test_seed))
    if check_seed_in_seeds(test_seed):
        #print("Seed " + str(test_seed) + " was tested as in the input seeds")
        break
    location += 1
    if location % 1000000 == 0:
        print("Locations processed so far " + str(location))

print("Smallest location " + str(location) + " found for seed " + str(test_seed))
