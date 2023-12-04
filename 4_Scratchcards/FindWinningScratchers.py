import sys

total_points = 0

def score_scratcher(line):
    card_points = 0
    removed_card_id = line.split(": ")[1]
    split1 = removed_card_id.split(" | ")

    winning_seq = split1[0]
    winning_nums = set()
    for num in winning_seq.split():
        winning_nums.add(int(num.strip()))

    game_seq = split1[1]
    game_nums = []
    for num in game_seq.split():
        game_nums.append(int(num.strip()))

    for num in game_nums:
        if num in winning_nums:
            if card_points == 0:
                card_points = 1
            else:
                card_points *= 2

    print(line + " scored " + str(card_points))
    return card_points

with open(sys.argv[1], "r", encoding="utf-8") as file:
    for line in file:
        total_points += score_scratcher(line)

print("Total points scored: " + str(total_points))