from collections import Counter

# Score categories
# Change the values as you see fit
YACHT = 12
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    if category <= 6:
        return sum([x for x in dice if x == category])
    elif category == 7:
        if sorted(Counter(dice).values()) == [2, 3]:
            return sum(dice)
        return 0
    elif category == 8:
        dice_groups = Counter(dice)
        for k, v in dice_groups.items():
            if v >= 4:
                return 4 * k
        return 0
    elif category == 9:
        if sorted(dice) == [1, 2, 3, 4, 5]:
            return 30
        return 0
    elif category == 10:
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30
        return 0
    elif category == 11:
        return sum(dice)
    elif category == 12:
        if len(Counter(dice)) == 1:
            return 50
        return 0