from game_manager import GameManager


if __name__ == '__main__':
    gm = GameManager()

    # Select player
    player = gm.players[0]

    # Draw five cards
    five_cards = gm.draw_five_cards(player)

    # Select card
    selected_card = gm.select_card(five_cards)

    # Execute the quest
    gm.execute_quest(player, selected_card)
