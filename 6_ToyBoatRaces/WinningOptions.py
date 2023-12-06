import sys

race_times = []
distance_records = []

# The toy car travels at a constant speed and suffers no drag in the easy version
def race_outcome(time, charge):
    go_time = time - charge
    return go_time * charge

with open(sys.argv[1], "r", encoding="utf-8") as file:
    time_line = file.readline()
    times = time_line.split(": ")[1]
    times = times.split()
    for time in times:
        race_times.append(int(time))

    distance_line = file.readline()
    distances = distance_line.split(": ")[1]
    distances = distances.split()
    for distance in distances:
        distance_records.append(int(distance))

# We're encouraged to take a brute force approach here in the simple one...
i = 0
wins = 0
winning_options = []
for race_time in race_times:
    wins = 0
    for charge in range(1, race_time): #OK to ignore the goes nowhere options
        distance_outcome = race_outcome(race_time, charge)
        if distance_outcome > distance_records[i]:
            #print("Winning option (time, charge): " + str(race_time) + ", " + str(charge) + " with new record " + str(distance_outcome))
            wins += 1
    winning_options.append(wins)
    i += 1

winning_product = 1
for item in winning_options:
    winning_product *= item

print("Product of winning options: " + str(winning_product))