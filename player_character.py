from config import HOMETOWN_BASELINE_ABILITY_VALUES
import random


class PlayerCharacter:
    def __init__(self, hometown):
        self.hp = 5
        self.rep_rank = 3
        self.abilities = {
            "STA": HOMETOWN_BASELINE_ABILITY_VALUES[hometown]["STA"],
            "POW": HOMETOWN_BASELINE_ABILITY_VALUES[hometown]["POW"],
            "AGI": HOMETOWN_BASELINE_ABILITY_VALUES[hometown]["AGI"],
            "CHI": HOMETOWN_BASELINE_ABILITY_VALUES[hometown]["CHI"],
            "WIT": HOMETOWN_BASELINE_ABILITY_VALUES[hometown]["WIT"],
        }

    def __str__(self):
        return \
            "Your abilities are:\n" +\
            "STA: " + str(self.abilities["STA"]) + "\n" +\
            "POW: " + str(self.abilities["POW"]) + "\n" +\
            "AGI: " + str(self.abilities["AGI"]) + "\n" +\
            "CHI: " + str(self.abilities["CHI"]) + "\n" +\
            "WIT: " + str(self.abilities["WIT"])

    def embark_quest(self, quest):
        attempt1 = self.abilities[quest.step_one["abilities"][0]] + self.abilities[quest.step_one["abilities"][1]] + random.randint(1, 6)
        if attempt1 >= quest.difficulty_class:
            print("You are succeeding.")
            attempt2 = self.abilities[quest.step_two["abilities"][0]] + self.abilities[quest.step_two["abilities"][1]] + random.randint(1, 6)
            if attempt2 >= quest.difficulty_class:
                quest.available = False
                self.rep_rank += 1
                print("You succeeded. Your reputation is increasing.")
                return
        self.rep_rank -= 1
        print("You failed. Fuck you.")
