from player_character import PlayerCharacter
from quest import Quest


def ask_player_for_action_choice():
    print(f"What would you like to do?")
    return Quest()


def display_info_of_quest(quest):
    print(f"You chose {quest.name}. {quest.description}")
    print(f'STEP ONE: {quest.step_one["description"]} {quest.step_one["abilities"][0]} + {quest.step_one["abilities"][1]}')
    print(f'STEP TWO: {quest.step_two["description"]} {quest.step_two["abilities"][0]} + {quest.step_two["abilities"][1]}')


if __name__ == '__main__':
    hometown = "Blackstone"
    pc = PlayerCharacter(hometown)
    print(pc); print()

    quest = ask_player_for_action_choice(); print()
    display_info_of_quest(quest); print()

    pc.embark_quest(quest); print()
    print(f'Rep rank: {pc.rep_rank}'); print(f'Techniques: {pc.techniques}')
