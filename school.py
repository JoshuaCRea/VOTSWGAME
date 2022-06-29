import random
from quest_card import QuestCard


class School:
    def __init__(self, name):
        self.name = name
        self.quest_cards = self._create_quest_cards()

    def _create_quest_cards(self):
        list_of_cards = [QuestCard(self.name) for _ in range(20)]
        return list_of_cards

    def present_quest_cards(self):
        cards_to_draw = 5
        random.shuffle(self.quest_cards)
        return self.quest_cards[:cards_to_draw]
