from player_character import PlayerCharacter
from school import School


class GameManager:
    def __init__(self):
        self.players = []
        self.schools = []
        self._setup_game()

    def _setup_game(self):
        self.players.append(PlayerCharacter("Blackstone"))
        self.players.append(PlayerCharacter("Fangmarsh"))
        self.players.append(PlayerCharacter("Leap-Creek"))
        self.players.append(PlayerCharacter("Pouch"))
        self.players.append(PlayerCharacter("Underclaw"))

        self.schools.append(School("School of Hong Quan"))
        self.schools.append(School("Temple of T'ai Chi Ch'uan"))
        self.schools.append(School("School of Zui Quan"))
        self.schools.append(School("Kwoon of Pai Tong Long"))
        self.schools.append(School("Kwoon of Changquan"))
