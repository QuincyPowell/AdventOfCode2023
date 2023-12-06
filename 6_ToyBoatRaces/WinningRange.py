import sys

race_time = 0
distance_record = 0

def race_outcome(time, charge):
    go_time = time - charge
    return go_time * charge

with open(sys.argv[1], "r", encoding="utf-8") as file:
    time_line = file.readline()
    times = time_line.split(": ")[1]
    times = times.split()
    clarified_race_time = ""
    for time in times:
        clarified_race_time += time
    race_time = int(clarified_race_time)

    distance_line = file.readline()
    distances = distance_line.split(": ")[1]
    distances = distances.split()
    clarified_race_distance = ""
    for distance in distances:
        clarified_race_distance += distance
    distance_record = int(clarified_race_distance)

# Linear search could be improved with a modified binary search
# Start with losing charge times
lowest_winning_charge = 0
highest_winning_charge = race_time
searching = True
while searching:
    lowest_winning_charge += 1
    outcome = race_outcome(race_time, lowest_winning_charge)
    if outcome > distance_record:
        searching = False
searching = True
while searching:
    highest_winning_charge -= 1
    outcome = race_outcome(race_time, highest_winning_charge)
    if outcome > distance_record:
        searching = False

winning_options = highest_winning_charge - lowest_winning_charge + 1
print("Based on a linear range search there are " + str(winning_options) + " winning options.")