import sys

total_min_power = 0

with open(sys.argv[1], "r", encoding="utf-8") as file:
    for line in file:
        min_cubes = {"red": 0, "green": 0, "blue": 0}
        split1 = line.split(": ")
        draws = split1[1].split("; ")
        for draw in draws:
            cubes = draw.split(", ")
            for cube in cubes:
                split2 = cube.split(" ")
                number = int(split2[0])
                color = split2[1].strip()
                if min_cubes[color] < number:
                    min_cubes[color] = number
        print(line)
        print("min red: " + str(min_cubes["red"]) + " min green: " + str(min_cubes["green"]) + " min blue: " + str(min_cubes["blue"]))
        total_min_power += min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]

print("total minimum power from all games: " + str(total_min_power))