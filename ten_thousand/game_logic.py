import random
from collections import Counter


# noinspection PyUnreachableCode
class GameLogic:


    @staticmethod
    def calculate_score(roll_dice):

        count = Counter(roll_dice)
        print(count)
        score = 0
        length_of_counter = len(count)

        if count[5] == 1 or count[5] == 2:
            score += 50 * count[5]

        if count[1] == 1 or count[1] == 2:
            score += 100 * count[1]

        for i in range(1, 7):
            if i == 1 and count[1] == 3:
                score += 1000
            elif i != 1 and count[i] == 3:
                score += i * 100

        for i in range(1, 7):
            if i == 1 and count[1] == 4:
                score += 2000
            elif i != 1 and count[i] == 4:
                score += i * 200

        for i in range(1, 7):
            if i == 1 and count[1] == 5:
                score += 3000
            elif i != 1 and count[i] == 5:
                score += i * 300

        for i in range(1, 7):
            if i == 1 and count[1] == 6:
                score += 4000
            elif i != 1 and count[i] == 6:
                score += i * 400

        for i in range(1, 7):
            if length_of_counter == 6 and count[i] == 1:
                score = 1500

        tally_three_pair = 0
        for i in range(1, 7):

            if count[i] == 2:
                tally_three_pair += 1
            if tally_three_pair == 3:
                score = 1500

        return score

        @staticmethod
        def roll_dice(rolled_dice):
            dice_list = []
            for _ in range(rolled_dice):
                dice_list.append(random.randint(1, 6))
            return tuple(dice_list)


