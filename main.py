from player_character import PlayerCharacter
from quest_card import QuestCard
import random


def generate_twenty_quest_cards():
    return [QuestCard() for _ in range(20)]


def generate_five_quest_cards(cards):
    random.shuffle(cards)
    return cards[:5]


def display_info_of_quest_card(quest_card):
    print(f'Chosen Card:\n{quest_card}')


def display_pertinent_quest_card_info(cards):
    for card in cards:
        abilities = [card.step_one["abilities"][0], card.step_one["abilities"][1], card.step_two["abilities"][0], card.step_two["abilities"][1]]
        print(f'{card.name}, {card.difficulty_class}, {abilities}, {card.rewards}')


if __name__ == '__main__':
    pc = PlayerCharacter("Blackstone")
    print(pc)

    twenty_quest_cards = generate_twenty_quest_cards(); print()
    display_pertinent_quest_card_info(twenty_quest_cards); print()
    five_quest_cards = generate_five_quest_cards(twenty_quest_cards); print()
    display_pertinent_quest_card_info(five_quest_cards); print()

    quest_card = random.choice(five_quest_cards)
    display_info_of_quest_card(quest_card)

    pc.embark_quest(quest_card); print()
    print(f'Rep rank: {pc.rep_rank}'); print(f'Techniques: {pc.techniques}')
