from player_character import PlayerCharacter
from quest_card import QuestCard
import random


def generate_five_quest_cards():
    return [QuestCard() for _ in range(5)]


def display_info_of_quest_card(quest_card):
    print(f'Chosen Card:\n{quest_card}')


def display_pertinent_quest_card_info(quest_cards):
    for card in quest_cards:
        abilities = [card.step_one["abilities"][0], card.step_one["abilities"][1], card.step_two["abilities"][0], card.step_two["abilities"][1]]
        print(f'{card.name}, {card.difficulty_class}, {abilities}, {card.rewards}')


if __name__ == '__main__':
    pc = PlayerCharacter("Blackstone")
    print(pc); print()

    five_quest_cards = generate_five_quest_cards(); print()
    display_pertinent_quest_card_info(five_quest_cards); print()

    quest_card = random.choice(five_quest_cards)
    display_info_of_quest_card(quest_card)

    pc.embark_quest(quest_card); print()
    print(f'Rep rank: {pc.rep_rank}'); print(f'Techniques: {pc.techniques}')
