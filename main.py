from player_character import PlayerCharacter
from quest_card import QuestCard


def ask_player_for_action_choice():
    print(f"What would you like to do?")
    return QuestCard()


def display_info_of_quest(quest_card):
    print(f'You chose {quest_card}')


if __name__ == '__main__':
    pc = PlayerCharacter("Blackstone")
    print(pc); print()

    quest_card = ask_player_for_action_choice(); print()
    display_info_of_quest(quest_card)

    pc.embark_quest(quest_card); print()
    print(f'Rep rank: {pc.rep_rank}'); print(f'Techniques: {pc.techniques}')
