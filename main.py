from player_character import PlayerCharacter
from quest import Quest


hometown = "Blackstone"
pc = PlayerCharacter(hometown)
catch_a_chicken = Quest()

print("Welcome to the Valley of the Silver Wolf!")
print(f"You are in {hometown}. What would you like to do? \n Options: 1. Draw Quests")
print(pc)
print("You chose Catch a Chicken. Some old bitch lost one of her cuccos. She tasks you with chasing it down and bringing it back.\n STEP ONE: Chase it down. STA + AGI")
print(f'Rep rank: {pc.rep_rank}')
pc.embark_quest(catch_a_chicken)
print(f'Rep rank: {pc.rep_rank}')
print(f'Is quest available? {catch_a_chicken.available}')