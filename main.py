from player_character import PlayerCharacter
import random

from school import School


if __name__ == '__main__':
    pc = PlayerCharacter("Blackstone")
    print(pc)
    school = School()

    five_quest_cards = school.present_quest_cards()
    for card in five_quest_cards:
        print(card.get_preview_of_card())

    quest_card = random.choice(five_quest_cards)
    print(quest_card.get_preview_of_card())

    pc.embark_quest(quest_card); print()
    print(f'Rep rank: {pc.rep_rank}'); print(f'Techniques: {pc.techniques}')
