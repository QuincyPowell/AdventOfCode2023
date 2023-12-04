import sys

total_scratch_cards = 0
scratch_card_stack = []
original_card_scores = {}

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
            card_points += 1

    # print(line + " scored " + str(card_points))
    return card_points

# Using a memoization optimization, first score all the cards
with open(sys.argv[1], "r", encoding="utf-8") as file:
    card_id = 1
    for line in file:
        score = score_scratcher(line)
        original_card_scores[card_id] = score
        card_id += 1

# Next use stack based recursion to determine how big that pile of scratchers is. Depth first approach.
# First add all the original scratchers to the stack
for key in original_card_scores:
    scratch_card_stack.append(key)

# Next recursively process them
while scratch_card_stack:
    total_scratch_cards += 1
    current_id = scratch_card_stack.pop()
    card_score = original_card_scores[current_id]
    while (card_score > 0):
        scratch_card_stack.append(current_id + card_score)
        card_score -= 1

print("Total scratch cards: " + str(total_scratch_cards))