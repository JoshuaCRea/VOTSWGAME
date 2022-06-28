class Quest:
    def __init__(self):
        self.name = "Catch a Chicken"
        self.description = "Some old bitch lost one of her cuccos. She tasks you with chasing it down and bringing it back."
        self.step_one = {
            "description": "Chase it down.",
            "abilities": ("STA", "AGI")
        }
        self.step_two = {
            "description": "Keep it calm as you carry it back.",
            "abilities": ("CHI", "WIT")
        }
        self.difficulty_class = 5
