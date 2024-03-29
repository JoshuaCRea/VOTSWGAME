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
        self.techniques = []

    def __str__(self):
        return \
            f'Reputation rank: {self.rep_rank}\n' +\
            f'Techniques: {self.techniques}\n' +\
            "Your abilities are:\n" +\
            f'STA: {str(self.abilities["STA"])}\n' +\
            f'POW: {str(self.abilities["POW"])}\n' +\
            f'AGI: {str(self.abilities["AGI"])}\n' +\
            f'CHI: {str(self.abilities["CHI"])}\n' +\
            f'WIT: {str(self.abilities["WIT"])}'

    def embark_quest(self, quest_card):
        print(quest_card.__repr__) # TODO remove
        if self._calculate_attempt_score(quest_card.step_one) >= quest_card.difficulty_class:
            print("SUCCESS Step One.")
            if self._calculate_attempt_score(quest_card.step_two) >= quest_card.difficulty_class:
                self._quest_won(quest_card.rewards["technique"])
                return
        self._quest_failed()

    def _calculate_attempt_score(self, quest_step):
        return self.abilities[quest_step["abilities"][0]] +\
               self.abilities[quest_step["abilities"][1]] +\
               random.randint(1, 6)

    def _quest_won(self, technique):
        print("SUCCESS Step Two. Your reputation increased.")
        self.rep_rank += 1
        self.techniques.append(technique)

    def _quest_failed(self):
        self.rep_rank -= 1
        print("You failed. Fuck you.")
