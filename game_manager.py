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
        self.players.append(PlayerCharacter("Blackstone", self.display))
        self.players.append(PlayerCharacter("Fangmarsh", self.display))
        self.players.append(PlayerCharacter("Leap-Creek", self.display))
        self.players.append(PlayerCharacter("Pouch", self.display))
        self.players.append(PlayerCharacter("Underclaw", self.display))

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
        for card in five_cards:
            self.display.notify(card.get_preview())
        return five_cards

    def select_card(self, cards):
        self.display.notify("Please select a card.")
        selected_card_number = random.randint(0, 4) # TODO Ask for user input
        selected_card = cards[selected_card_number]
        self.display.notify(f'You selected {selected_card}')
        return selected_card

    def execute_quest(self, player, card):
        player.embark_quest(card)
