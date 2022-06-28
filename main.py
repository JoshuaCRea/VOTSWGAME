from player_character import PlayerCharacter
from quest import Quest


hometown = "Blackstone"
pc = PlayerCharacter(hometown)
quest = Quest()

print("**** Welcome to the Valley of the Silver Wolf! ****")
print(f"You are in {hometown}. What would you like to do?")
print(pc)
print(f"Options: 1. Draw Quests")
print(f"You chose {quest.name}. {quest.description}")
print(f'STEP ONE: {quest.step_one["description"]} {quest.step_one["abilities"][0]} + {quest.step_one["abilities"][1]}')
print(f'STEP TWO: {quest.step_two["description"]} {quest.step_two["abilities"][0]} + {quest.step_two["abilities"][1]}')
print(f'Rep rank: {pc.rep_rank}')
pc.embark_quest(quest)
print(f'Rep rank: {pc.rep_rank}')
