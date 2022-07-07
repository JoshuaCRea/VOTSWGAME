from config import HOMETOWN_BASELINE_ABILITY_VALUES
import random
from config import LOCATION_MAP

class PlayerCharacter:
    def __init__(self, hometown, event_observer):
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
        self.location = hometown
        self.event_observer = event_observer

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
        if self._calculate_attempt_score(quest_card.step_one) >= quest_card.difficulty_class:
            self.event_observer.notify("You succeeded on the first step.")
            if self._calculate_attempt_score(quest_card.step_two) >= quest_card.difficulty_class:
                self._quest_won(quest_card)
                return
        self._quest_failed()

    def _calculate_attempt_score(self, quest_step):
        return self.abilities[quest_step["abilities"][0]] +\
               self.abilities[quest_step["abilities"][1]] +\
               random.randint(1, 6)

    def _quest_won(self, quest_card):
        self.event_observer.notify(f'You succeeded on the second step. Your reputation increased and you acquired {quest_card.rewards["technique"]}.')
        self.rep_rank += 1
        self.techniques.append(quest_card.rewards["technique"])
        self.event_observer.discontinue_quest(self.location, quest_card)
        if quest_card.rewards["stat_bonus"] != None:
            self.abilities[quest_card.rewards["stat_bonus"]] += 1

    def _quest_failed(self):
        self.rep_rank -= 1
        self.event_observer.notify("You failed. Fuck you.")

    def move_player(self, direction):
        start = LOCATION_MAP[self.location][1]
        end = (start + direction) % len(LOCATION_MAP)
        for key, value in LOCATION_MAP.items():
            if value[1] == end:
                self.location = key
