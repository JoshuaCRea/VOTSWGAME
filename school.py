from quest_card import QuestCard


class School:
    def __init__(self, name):
        self.name = name
        self.quest_cards = self._create_quest_cards()

    def _create_quest_cards(self):
        list_of_cards = [QuestCard(self.name) for _ in range(20)]
        return list_of_cards