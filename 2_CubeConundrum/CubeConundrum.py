import sys

CONSTRAINTS = {"red": 12, "green": 13, "blue": 14}

sum_possible_gameid = 0

with open(sys.argv[1], "r", encoding="utf-8") as file:
    for line in file:
        game_follows_constraints = True
        split1 = line.split(": ")
        game_id = int(split1[0][5:])
        games = split1[1].split("; ")
        for game in games:
            cubes = game.split(", ")
            for cube in cubes:
                split2 = cube.split(" ")
                number = int(split2[0])
                color = split2[1].strip()
                if CONSTRAINTS[color] < number:
                    print(cube.strip() + " violated " + str(number) + " <= " + str(CONSTRAINTS[color]))
                    game_follows_constraints = False
        if game_follows_constraints:
            print(line + " followed constraints" + " adding " + str(game_id))
            sum_possible_gameid += game_id
        else:
            print(line + " contained constraint violation")

print ("Sum of games that followed constraints: " + str(sum_possible_gameid))