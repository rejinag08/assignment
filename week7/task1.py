import random

def roll_dice():
    return random.randint(1, 6)

def main_dice_roll():
    result = 0
    rolls = []  # To keep track of all roll results
    while result != 6:
        result = roll_dice()
        rolls.append(result)
        print("rolls:", result)
    return rolls
