class Quest:
    def __init__(self):
        self.name = "The Walls of Blackstone"
        self.description = "Learn defensive techniques by helping the laborers of Blackstone School build a defensive structure of stone and metal."
        self.step_one = {
            "description": "Carry the heavy dark stones up the ladder to the top of the new outer wall around the school.",
            "abilities": ("STA", "POW")
        }
        self.step_two = {
            "description": "Practice defensive movements by spreading the mortar quickly in the hot dry sun, and putting the stones in place.",
            "abilities": ("STA", "CHI")
        }
        self.difficulty_class = 4
        self.reward = "Stone Paw, Iron Beak"
