class PlayerCharacter:
    def __init__(self):
        self.hp = 5
        self.standing = True

    def receive_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.standing = False