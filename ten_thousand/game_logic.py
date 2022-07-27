import random
import collections
from collections import Counter

class GameLogic:
    def __init__(self, roll, calculate):
        self.head = None
        self.roll = roll

    @staticmethod
    def roll_dice(roll):
        # if roll == None:
        #     roll = roll
        if roll == 0:
            return()
        dice_roll = tuple(random.randint(1, 6) for i in range(roll))
        return dice_roll

# create variable to handle argument passed into method

    @staticmethod
    def calculate_score(dice):
        count = Counter(dice)
        if len(count) == 6:
            return 1500
        if len(count) == 3 and all(val == 2 for val in count.values()):
            return 1500

        score = 0

        dice_used = five_used = False

        for num in range(1, 6 + 1):
            number_count = count[num]
            if number_count >= 3:
                if num == 1:
                    dice_used = True
                elif num == 5:
                    five_used = True
                    score += num * 100
                    egg = number_count - 3
                    score += score * egg


        return score








