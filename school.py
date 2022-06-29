import random
from quest_card import QuestCard


class School:
    def __init__(self):
        self.quest_cards = [QuestCard() for _ in range(20)]

    def present_quest_cards(self):
        cards_to_draw = 5
        random.shuffle(self.quest_cards)
        return self.quest_cards[:cards_to_draw]
