import random
from display import Display
from player_character import PlayerCharacter
from school import School


class GameManager:
    def __init__(self):
        self.players = []
        self.schools = {}
        self.display = Display()
        self._setup_game()

    def _setup_game(self):
        self.players = [
            PlayerCharacter("Blackstone", self.display),
            PlayerCharacter("Fangmarsh", self.display),
            PlayerCharacter("Leap-Creek", self.display),
            PlayerCharacter("Pouch", self.display),
            PlayerCharacter("Underclaw", self.display),
        ]
        self.schools = {
            "Blackstone": School("School of Hong Quan"),
            "Fangmarsh": School("Temple of T'ai Chi Ch'uan"),
            "Leap-Creek": School("School of Zui Quan"),
            "Pouch": School("Kwoon of Pai Tong Long"),
            "Underclaw": School("Kwoon of Changquan"),
        }

    def draw_five_cards(self, player):
        school = self.schools[player.location]
        random.shuffle(school.quest_cards)
        five_cards = school.quest_cards[:5]
        filtered_cards = []
        for card in five_cards:
            if card.rep_req <= player.rep_rank:
                filtered_cards.append(card)
                self.display.notify(card.get_preview())
        if len(filtered_cards) == 0:
            raise Exception(f'Player cannot play any of the drawn cards because their repuation rank is too low (rep rank: {player.rep_rank}).')
        return filtered_cards

    def select_card(self, cards):
        self.display.notify("Please select a card.")
        selected_card_number = random.randint(0, len(cards) - 1)
        selected_card = cards[selected_card_number]
        self.display.notify(f'You selected {selected_card}')
        return selected_card

    def execute_quest(self, player, card):
        player.embark_quest(card)
