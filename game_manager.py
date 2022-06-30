import random
from config import LOCATION_MAP
from player_character import PlayerCharacter
from school import School


class GameManager:
    def __init__(self):
        self.players = []
        self.schools = {}
        self._setup_game()

    def _setup_game(self):
        self.players = [
            PlayerCharacter("Blackstone", self),
            PlayerCharacter("Fangmarsh", self),
            PlayerCharacter("Leap-Creek", self),
            PlayerCharacter("Pouch", self),
            PlayerCharacter("Underclaw", self),
        ]
        self.schools = {
            "Blackstone": School("School of Hong Quan"),
            "Fangmarsh": School("Temple of T'ai Chi Ch'uan"),
            "Leap-Creek": School("School of Zui Quan"),
            "Pouch": School("Kwoon of Pai Tong Long"),
            "Underclaw": School("Kwoon of Changquan"),
        }

    def draw_quest_cards(self, player):
        school = self.schools[player.location]
        random.shuffle(school.quest_cards)
        drawn_cards = school.quest_cards[:5]
        self.notify("\nFirst drawn 5")
        for card in drawn_cards:
            self.notify(card.get_preview())
        filtered_cards = self._filter_drawn_quest_cards(player, drawn_cards)
        return filtered_cards

    def _filter_drawn_quest_cards(self, player, drawn_cards):
        filtered_cards = []
        self.notify("\nThese are the filtered cards.")
        for card in drawn_cards:
            if card.rep_req <= player.rep_rank:
                filtered_cards.append(card)
                self.notify(card.get_preview())
        if len(filtered_cards) == 0:
            raise Exception(f'Player cannot play any of the drawn cards because their reputation rank is too low (rep rank: {player.rep_rank}).')
        return filtered_cards

    def select_card(self, cards):
        self.notify("\nPlease select a card...")
        selected_card_number = random.randint(0, len(cards) - 1)
        selected_card = cards[selected_card_number]
        self.notify(f'You selected {selected_card}')
        return selected_card

    def execute_quest(self, player, card):
        player.embark_quest(card)

    def discontinue_quest(self, location, quest_card):
        school = self.schools[location]
        school.quest_cards.remove(quest_card)

    def notify(self, *messages):
        for message in messages:
            print(message)

    def move_player(self, player, direction):
        start = LOCATION_MAP[player.location][1]
        end = (start + direction) % len(LOCATION_MAP)
        for key, value in LOCATION_MAP.items():
            if value[1] == end:
                player.location = key
