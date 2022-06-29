from uuid import uuid4

from config import SCHOOL_NAME_QUEST_CARD_MAP


class QuestCard:
    def __init__(self, school_name):
        self.name = SCHOOL_NAME_QUEST_CARD_MAP[school_name]["name"] + str(uuid4())[:8]
        self.description = SCHOOL_NAME_QUEST_CARD_MAP[school_name]["description"]
        self.step_one = {
            "description": SCHOOL_NAME_QUEST_CARD_MAP[school_name]["step_one"]["description"],
            "abilities": SCHOOL_NAME_QUEST_CARD_MAP[school_name]["step_one"]["abilities"],
        }
        self.step_two = {
            "description": SCHOOL_NAME_QUEST_CARD_MAP[school_name]["step_two"]["description"],
            "abilities": SCHOOL_NAME_QUEST_CARD_MAP[school_name]["step_two"]["abilities"],
        }
        self.difficulty_class = SCHOOL_NAME_QUEST_CARD_MAP[school_name]["difficulty_class"]
        self.rewards = {
            "technique": SCHOOL_NAME_QUEST_CARD_MAP[school_name]["rewards"]["technique"],
            "stat_bonus": SCHOOL_NAME_QUEST_CARD_MAP[school_name]["rewards"]["stat_bonus"]
        }

    def __str__(self):
        return f'{self.name}\n{self.description}\n' +\
               f'STEP ONE: {self.step_one["description"]} {self.step_one["abilities"][0]} + {self.step_one["abilities"][1]}\n' +\
               f'STEP TWO: {self.step_two["description"]} {self.step_two["abilities"][0]} + {self.step_two["abilities"][1]}\n'

    def get_preview_of_card(self):
        abilities = [self.step_one["abilities"][0], self.step_one["abilities"][1], self.step_two["abilities"][0], self.step_two["abilities"][1]]
        return f'{self.name}, {self.difficulty_class}, {abilities}, {self.rewards}'