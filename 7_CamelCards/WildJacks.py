import sys

# This is a bit of a hack so that the string will sort how we want it to
def translate_face(hand):
    translated_hand = ""
    cursor = 0
    end = 5
    translation_dict = {"T": "A", "J": "1", "Q": "C", "K": "D", "A": "E"}

    if len(hand) != end:
        print("Invalid hand, should have exactly 5 cards.")
        return None

    while cursor < end:
        if hand[cursor] in translation_dict:
            translated_hand += translation_dict[hand[cursor]]
        else:
            translated_hand += hand[cursor]
        cursor += 1

    return translated_hand

def type_hand(hand):
    matches = {}
    wildcards = 0
    cursor = 0
    end = 5

    if len(hand) != end:
        print("Invalid hand, should have exactly 5 cards.")
        return None

    while cursor < end:
        if hand[cursor] == "J":
            wildcards += 1
        elif hand[cursor] in matches:
            matches[hand[cursor]] += 1
        else:
            matches[hand[cursor]] = 1
        cursor += 1

    large_pair_count = 0
    small_pair_count = 0
    for count in matches.values():
        if count >= large_pair_count:
            small_pair_count = large_pair_count
            large_pair_count = count
        elif count > small_pair_count:
            small_pair_count = count

    if wildcards == 5:
        large_pair_count = 5
    else:
        large_pair_count += wildcards

    if large_pair_count == 5:
        return 7
    elif large_pair_count == 4:
        return 6
    elif large_pair_count == 3 and small_pair_count == 2:
        return 5
    elif large_pair_count == 3:
        return 4
    elif large_pair_count == 2 and small_pair_count == 2:
        return 3
    elif large_pair_count == 2:
        return 2
    else:
        return 1

hands = []
with open(sys.argv[1], "r", encoding="utf-8") as file:
    for line in file:
        split = line.split()
        hand = split[0]
        translated_hand = translate_face(hand)
        bid = int(split[1])
        hand_type = type_hand(hand)
        hands.append((hand_type, translated_hand, hand, bid))

hands.sort()

hand_rank = 0
total_winnings = 0
for hand in hands:
    hand_rank += 1
    print(hand)
    total_winnings += hand_rank * hand[3]

print("Total winnings: " + str(total_winnings))