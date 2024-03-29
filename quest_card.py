from uuid import uuid4


class QuestCard:
    def __init__(self):
        self.name = f"The Walls of Blackstone - {str(uuid4())[:8]}"
        self.description = "Learn defensive techniques by helping the laborers of Blackstone School build a defensive structure of stone and metal."
        self.step_one = {
            "description": "Carry the heavy dark stones up the ladder to the top of the new outer wall around the school.",
            "abilities": ("STA", "POW")
        }
        self.step_two = {
            "description": "Practice defensive movements by spreading the mortar quickly in the hot dry sun, and putting the stones in place.",
            "abilities": ("STA", "CHI")
        }
        self.difficulty_class = 0 # TODO changed to 0 for testing removal of card from school
        self.rewards = {
            "technique": "Stone Paw, Iron Beak",
            "stat_bonus": None
        }

    def __str__(self):
        return f'{self.name}\n{self.description}\n' +\
               f'STEP ONE: {self.step_one["description"]} {self.step_one["abilities"][0]} + {self.step_one["abilities"][1]}\n' +\
               f'STEP TWO: {self.step_two["description"]} {self.step_two["abilities"][0]} + {self.step_two["abilities"][1]}\n'

    def get_preview_of_card(self):
        abilities = [self.step_one["abilities"][0], self.step_one["abilities"][1], self.step_two["abilities"][0], self.step_two["abilities"][1]]
        return f'{self.name}, {self.difficulty_class}, {abilities}, {self.rewards}'